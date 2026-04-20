import pandas as pd
import glob
import os

arquivos = glob.glob("../data/GSE296007_RAW/*.txt.gz")
dados_agregados = {}

for arquivo in arquivos:
    nome_base = os.path.basename(arquivo)
    partes = nome_base.split("_")
    
    if len(partes) >= 2:
        grupo_tratamento = partes[1] 
    else:
        grupo_tratamento = "Desconhecido"
    
    df = pd.read_csv(arquivo, sep="\t", header=None, names=["gene_id", "contagem"], compression="gzip")
    df = df[~df["gene_id"].astype(str).str.startswith("__")]
    
    serie_contagem = df.set_index("gene_id")["contagem"]
    
    if grupo_tratamento in dados_agregados:
        dados_agregados[grupo_tratamento] = dados_agregados[grupo_tratamento].add(serie_contagem, fill_value=0)
    else:        dados_agregados[grupo_tratamento] = serie_contagem

tabela_final = pd.DataFrame(dados_agregados)
tabela_final = tabela_final.fillna(0).astype(int)
tabela_final.reset_index(inplace=True)

nome_saida = "../data/tabela_expressao_genica_microplastico.csv"
tabela_final.to_csv(nome_saida, index=False)
