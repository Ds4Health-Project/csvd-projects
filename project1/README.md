# Projeto Ciência de redes aplicada à toxicidade de microplásticos em pulmões humanos
# Project Network science applied to microplastic toxicity in human lungs

# Descrição Resumida do Projeto

Este projeto investiga a toxicidade respiratória de micro e nanoplásticos (MNPs), especificamente partículas de poliestireno, em fibroblastos pulmonares humanos (HPFs). Como o sistema respiratório distal carece de mecanismos eficientes de autolimpeza, a inalação torna-se uma via de exposição crítica, capaz de desencadear estresse celular e processos fibróticos. O estudo possui implicações profundas, pois adota uma abordagem sistêmica de ciência de redes para mapear como esses poluentes comprometem a robustez celular. Isso fornecerá uma compreensão inédita e estrutural sobre os mecanismos moleculares que impulsionam doenças respiratórias causadas pela exposição ao plástico.

A pergunta central da pesquisa busca entender como diferentes tamanhos de partículas de poliestireno (0,1 µm vs 1 µm) reconfiguram a topologia das redes de coexpressão gênica nestas células e quais genes centrais (hubs) controlam a transição para um estado de estresse celular. Trabalhando com a hipótese de que partículas menores afetam a função mitocondrial enquanto as maiores impactam a membrana e a homeostase proteica, o estudo aplicará metodologias avançadas (WGCNA e análise topológica) a dados de RNA-seq existentes. Essa abordagem permitirá identificar a hierarquia regulatória da resposta celular, avançando de forma original além da tradicional análise de genes isolados.

# Slides

* [Slides](project1/slides.pdf)

# Fundamentação Teórica

A inalação de micro e nanoplásticos (MNPs) representa uma via de exposição crítica, pois o sistema respiratório distal carece de mecanismos eficientes de autolimpeza. Os fibroblastos pulmonares humanos (HPFs) são células fundamentais na manutenção da integridade tecidual e na resposta a lesões, sendo os principais efetores no desenvolvimento de processos fibróticos. Evidências recentes indicam que a exposição ao poliestireno (PS) induz estresse oxidativo, disfunção mitocondrial e alteração na síntese proteica.

### Artigos de Base:
- Chwiej et al. (2025) [Série GSE296007]: Estudo central que fornece os dados de RNA-seq de HPFs expostos a partículas de 0,1 µm e 1 µm. https://doi.org/10.1038/s41598-025-22947-7
- Sainz et al. (2024): Referência metodológica para a aplicação de WGCNA e integração com redes de interação proteína-proteína (PPI).  https://doi.org/10.1186/s12870-024-05280-5 

# Perguntas de Pesquisa

### Pergunta: 
- De que maneira o tamanho das partículas de poliestireno (0,1 µm vs 1 µm) reconfigura a topologia das redes de coexpressão gênica em HPFs, e quais hubs controlam a transição para um fenótipo de estresse celular?
### Hipótese: 
- Espera-se que partículas menores desencadeiem respostas intracelulares associadas à função mitocondrial, enquanto partículas maiores possam modular processos relacionados à membrana celular e homeostase proteica.

# Bases de Dados

> Base de Dados | Endereço na Web | Resumo descritivo
> ----- | ----- | -----
> GSE296007 | https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE296007 | Breve resumo (duas ou três linhas) sobre a base.
> PRJNA868178 | https://www.ncbi.nlm.nih.gov/sra/?term=PRJNA868178 | Breve resumo (duas ou três linhas) sobre a base.

# Modelo Lógico

> ![Modelo Lógico de Grafos](images/modelo-logico-grafos.png)

# Metodologia

A metodologia integrará abordagens de transcriptômica e ciência de redes para mapear as respostas fenotípicas sistêmicas aos diferentes tamanhos de microplásticos, estruturando a pesquisa nas seguintes etapas:

**1. Aquisição e Pré-processamento dos Dados (RNA-seq):**
Os dados brutos e as matrizes de contagem serão obtidos a partir dos dados **PRJNA868178** e **GSE296007** utilizando ferramentas de extração como o SRA Toolkit. Após o controle de qualidade, quantificação e normalização dos dados para remover o viés de sequenciamento, buscaremos identificar quais genes são diferencialmente expressos nos HPFs frente à exposição às partículas de 0,1 µm e 1 µm em relação aos grupos controle.

**2. Construção das Redes de Coexpressão:**
Para responder como as partículas reconfiguram a topologia celular, utilizaremos as matrizes de expressão em redes onde os nós representam genes e as arestas representam a força de coexpressão entre eles, permitindo observar o sistema pulmonar de forma conectada e não como genes isolados.

**3. Técnicas de Ciência de Redes:**

* **Detecção de Comunidades:** Aplicaremos algoritmos para agrupar as redes em módulos de genes altamente conectados. Para testar a hipótese da pesquisa, extrairemos esses módulos e faremos análises de enriquecimento funcional (Gene Ontology e KEGG). A meta é verificar se os módulos associados à rede de partículas de 0,1 µm apresentam forte enriquecimento para "função mitocondrial", e se os módulos da rede de 1 µm concentram funções de "homeostase proteica" e "integridade de membrana".
* **Análise de Centralidade e Hubs:** Para descobrir quais hubs controlam o estado de estresse celular, calcularemos métricas de centralidade (Grau, Intermediação e Autovetor). Os genes com as maiores pontuações nesses módulos de estresse serão apontados como os reguladores moleculares primários da transição fibrótica.
* **Comparação Topológica:** Calcularemos métricas macroscópicas da rede como o coeficiente de agrupamento e o tamanho do caminho característico para demonstrar o nível de fragmentação ou resiliência da rede do hospedeiro quando exposta a diferentes tamanhos de partículas.

# Ferramentas

Durante todo o projeto, isso é desde a aquisição dos arquivos no SRA até a visualização topológica, utilizaremos as seguintes ferramentas tecnologias:

* **SRA Toolkit:** Essencial para o download e extração eficiente dos dados de sequenciamento brutos das bases públicas.
* **FastQC / Kallisto (ou STAR):** Ferramentas de bioinformática necessárias para o controle de qualidade e a quantificação/alinhamento das *reads* de RNA.
* **PyDESeq2:** Biblioteca em Python para análise de expressão gênica diferencial.
* **PyWGCNA:** Construção da rede ponderada de coexpressão gênica baseada na variância dos tratamentos.
* **NetworkX & Graph-Tool:** Bibliotecas centrais de Ciência de Redes para cálculos de centralidade, caminhos mínimos e aplicação de algoritmos de detecção de comunidades.
* **GSEApy:** Realização de análises de enriquecimento de vias (GO/KEGG) para validar as funções biológicas associadas às hipóteses propostas.
* **Py4Cytoscape:** Integração para renderização avançada da rede e customização de atributos visuais dos hubs.
* **Scanpy:** Para análises exploratórias avançadas de agrupamento.
* **Plotly:** Geração de gráficos estatísticos interativos associados às métricas topológicas da rede.

# Referências Bibliográficas

* Chwiej, J., et al. (2025). *Study on the respiratory toxicity of 0.1 µm and 1 µm polystyrene particles in human lung fibroblasts*. Gene Expression Omnibus, GSE296007. Disponível em: https://doi.org/10.1038/s41598-025-22947-7
* Sainz, M., et al. (2024). *Application of Weighted Gene Co-expression Network Analysis (WGCNA) and Protein-Protein Interaction networks*. BMC Plant Biology. Disponível em: https://doi.org/10.1186/s12870-024-05280-5
* Langfelder, P., & Horvath, S. (2008). *WGCNA: an R package for weighted correlation network analysis*. BMC Bioinformatics, 9(1), 559.
* Love, M. I., Huber, W., & Anders, S. (2014). *Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2*. Genome Biology, 15(12), 550.
* National Center for Biotechnology Information (NCBI). *Sequence Read Archive (SRA), Accession PRJNA868178*.