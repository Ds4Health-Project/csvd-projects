import os
import glob
import pandas as pd


def prepare_GEO_dataset(input_directory: str, output_path: str) -> pd.DataFrame:
    search_pattern = os.path.join(input_directory, "*.txt.gz")
    files = glob.glob(search_pattern)

    sample_data = {}

    for file in files:
        file_name = os.path.basename(file)
        column_name = file_name.replace(".txt.gz", "").replace("_count", "")

        parts = column_name.split("_")
        if len(parts) >= 2:
            column_name = "_".join(parts[1:])
        else:
            column_name = column_name

        df = pd.read_csv(
            file,
            sep="\t",
            header=None,
            names=["gene_id", "count"],
            compression="gzip",
        )
        df = df[~df["gene_id"].astype(str).str.startswith("__")]

        sample_data[column_name] = df.set_index("gene_id")["count"]

    final_table = pd.DataFrame(sample_data).fillna(0).astype(int)
    final_table.reset_index(inplace=True)

    return final_table


def load_dataframe(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)


def save_dataframe(df: pd.DataFrame, file_path: str):
    df.to_csv(file_path, index=False)

def save_module_gene_ids(module_dict: dict, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    
    for color, df in module_dict.items():
        file_path = os.path.join(output_dir, f"wgcna_module_{color}.csv")
        pd.Series(df.index, name="gene_id").to_csv(file_path, index=False)