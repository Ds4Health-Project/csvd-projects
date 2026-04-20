import pandas as pd
import numpy as np


df = pd.read_csv("../data/tabela_expressao_microplasticos.csv")

colunas_amostras = [col for col in df.columns if col != 'gene_id']
siglas_grupos = set([col.split("_")[0] for col in colunas_amostras])
siglas_tratamento = [g for g in siglas_grupos if g != "CTR"]

tabela_final = pd.DataFrame({"gene_id": df["gene_id"]})

colunas_ctr = [col for col in df.columns if col.startswith("CTR_")]
media_ctr = df[colunas_ctr].mean(axis=1) + 1

for grupo in siglas_tratamento:
    colunas_grupo = [col for col in df.columns if col.startswith(f"{grupo}_")]
    
    media_grupo = df[colunas_grupo].mean(axis=1) + 1
    fc = media_grupo / media_ctr
    log2fc = np.log2(fc)
    
    tabela_final[f"Log2FC_{grupo}"] = log2fc

nome_saida = "../data/tabela_Log2FC_microplasticos.csv"
tabela_final.to_csv(nome_saida, index=False)