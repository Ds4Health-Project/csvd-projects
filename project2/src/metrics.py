import os
import pandas as pd
import numpy as np
import PyWGCNA


def calculate_log2fc(
    df: pd.DataFrame, treatment_group: str, control_group: str = "CTR"
) -> pd.DataFrame:
    treatment_columns = [
        col for col in df.columns if col.startswith(f"{treatment_group}_")
    ]
    control_columns = [col for col in df.columns if col.startswith(f"{control_group}_")]

    treatment_mean = df[treatment_columns].mean(axis=1) + 1
    control_mean = df[control_columns].mean(axis=1) + 1
    log2fc_values = np.log2(treatment_mean / control_mean)

    fc_result = pd.DataFrame(
        {"gene_id": df["gene_id"], f"Log2FC_{treatment_group}": log2fc_values}
    )

    return fc_result


def filter_significant_genes(
    df: pd.DataFrame, target_column: str, threshold: float = None, top_n: int = None
) -> pd.DataFrame:
    if target_column not in df.columns:
        return None

    filtered_df = df.copy()

    if threshold is not None:
        filtered_df = filtered_df[
            (filtered_df[target_column] >= threshold)
            | (filtered_df[target_column] <= -threshold)
        ]

    if top_n is not None:
        filtered_df["abs_val"] = filtered_df[target_column].abs()
        filtered_df = filtered_df.nlargest(top_n, "abs_val").drop(columns=["abs_val"])

    return filtered_df

def run_pairwise_wgcna(counts_df: pd.DataFrame, treatment_prefix: str, control_prefix: str, top_n_genes: int, output_csv_path: str) -> dict:
    
    if "gene_id" in counts_df.columns:
        counts_df = counts_df.set_index("gene_id")

    treatment_cols = [col for col in counts_df.columns if col.startswith(f"{treatment_prefix}_")]
    control_cols = [col for col in counts_df.columns if col.startswith(f"{control_prefix}_")]
    
    pairwise_samples = control_cols + treatment_cols
    pairwise_df = counts_df[pairwise_samples]

    mad_genes = pairwise_df.apply(lambda x: np.median(np.abs(x - np.median(x))), axis=1)
    selected_genes = mad_genes.nlargest(top_n_genes).index
    filtered_df = pairwise_df.loc[selected_genes]

    wgcna_df = filtered_df.T

    trait_list = []
    for sample in wgcna_df.index:
        if sample.startswith(control_prefix):
            trait_list.append(0)
        elif sample.startswith(treatment_prefix):
            trait_list.append(1)

    traits_df = pd.DataFrame({"Treatment_Status": trait_list}, index=wgcna_df.index)

    network_name = f"WGCNA_{treatment_prefix}_vs_{control_prefix}"
    print(f"\nBuilding Network: {network_name} with {len(wgcna_df.index)} samples...")
    
    network = PyWGCNA.WGCNA(name=network_name, species="Mus musculus", 
                            geneExp=wgcna_df, save=False)
    
    network.preprocess()
    network.findModules()
    network.updateSampleInfo(sampleInfo=traits_df)

    module_colors = network.datExpr.var['moduleColors']

    result_df = pd.DataFrame({
        "gene_id": wgcna_df.columns, 
        "WGCNA_Module": module_colors.values
    })
    result_df.to_csv(output_csv_path, index=False)
    print(f"Master file saved to: {output_csv_path}")

    module_dfs_dict = {}
    unique_colors = module_colors.unique()
    
    for color in unique_colors:
        color_genes = module_colors[module_colors == color].index
        module_dfs_dict[color] = filtered_df.loc[color_genes].copy()
        
    return module_dfs_dict
