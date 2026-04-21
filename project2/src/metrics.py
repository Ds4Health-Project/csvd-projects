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
