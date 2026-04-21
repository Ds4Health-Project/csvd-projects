import pandas as pd
import numpy as np


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
    df: pd.DataFrame, target_column: str, threshold: float = 1.0
) -> pd.DataFrame:
    filtered_genes = df[
        (df[target_column] >= threshold) | (df[target_column] <= -threshold)
    ].copy()

    original_count = len(df)
    final_count = len(filtered_genes)
    print(f"Genes discarded: {original_count - final_count}")

    return filtered_genes
