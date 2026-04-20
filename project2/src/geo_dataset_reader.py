import pandas as pd
import glob
import os

arquivos = glob.glob("../data/GSE296007_RAW/*.txt.gz")

dados_amostras = {}
for arquivo in arquivos:
    nome_base = os.path.basename(arquivo)
    
    partes = nome_base.split("_")
    if len(partes) >= 3:
        nome_coluna = f"{partes[1]}_{partes[2]}" 
    else:
        nome_coluna = partes[0]
        
    df = pd.read_csv(arquivo, sep="\t", header=None, names=["gene_id", "contagem"], compression="gzip")
    df = df[~df["gene_id"].astype(str).str.startswith("__")]
    
    dados_amostras[nome_coluna] = df.set_index("gene_id")["contagem"]

tabela_final = pd.DataFrame(dados_amostras)
tabela_final.reset_index(inplace=True)

nome_saida = "../data/tabela_expressao_microplasticos.csv"
tabela_final.to_csv(nome_saida, index=False)