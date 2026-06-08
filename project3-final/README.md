# Projeto Ciência de redes aplicada à toxicidade de microplásticos em pulmões humanos

# Project Network science applied to microplastic toxicity in human lungs

# Descrição Resumida do Projeto

Este projeto investiga a toxicidade respiratória de micro e nanoplásticos (MNPs), especificamente partículas de poliestireno, em fibroblastos pulmonares humanos (HPFs). Como o sistema respiratório distal carece de mecanismos eficientes de autolimpeza, a inalação torna-se uma via de exposição crítica, capaz de desencadear estresse celular e processos fibróticos. O estudo possui implicações profundas, pois adota uma abordagem sistêmica de ciência de redes para mapear como esses poluentes comprometem a robustez celular. Isso fornecerá uma compreensão estrutural sobre os mecanismos moleculares que impulsionam doenças respiratórias causadas pela exposição ao plástico.

A pergunta central da pesquisa busca entender como diferentes tamanhos de partículas de poliestireno (0,1 µm vs 1 µm) reconfiguram a topologia das redes de coexpressão gênica nestas células e quais genes centrais (hubs) controlam a transição para um estado de estresse celular. Trabalhando com a hipótese de que partículas menores afetam a função mitocondrial enquanto as maiores impactam a membrana e a homeostase proteica, o estudo aplicará metodologias avançadas (WGCNA e análise topológica) a dados de RNA-seq existentes. Essa abordagem permitirá identificar a hierarquia regulatória da resposta celular, avançando de forma original além da tradicional análise de genes isolados.

# Slides

- [Slides](assets/slides/apresentacao.pdf)

# Fundamentação Teórica

A inalação de micro e nanoplásticos (MNPs) representa uma via de exposição crítica, pois o sistema respiratório distal carece de mecanismos eficientes de autolimpeza. Os fibroblastos pulmonares humanos (HPFs) são células fundamentais na manutenção da integridade tecidual e na resposta a lesões, sendo os principais efetores no desenvolvimento de processos fibróticos. Evidências recentes indicam que a exposição ao poliestireno (PS) induz estresse oxidativo, disfunção mitocondrial e alteração na síntese proteica.

O estudo de Chwiej et al. (2025) mostrou que partículas de poliestireno de 100 nm e 1 µm induzem alterações transcriptômicas distintas em HPFs, sugerindo que o tamanho da partícula influencia mecanismos celulares diferentes. Em paralelo, o trabalho de Sainz et al. (2024) oferece uma base metodológica útil ao demonstrar como análises integradas de expressão diferencial, WGCNA, enriquecimento funcional e redes de interação proteína-proteína podem revelar módulos biologicamente relevantes e hub de genes.

## Artigos de Base:

- Chwiej et al. (2025) [Série GSE296007]: Estudo central que fornece os dados de RNA-seq de HPFs expostos a partículas de 0,1 µm e 1 µm. https://doi.org/10.1038/s41598-025-22947-7
- Sainz et al. (2024): Referência metodológica para a aplicação de WGCNA e integração com redes de interação proteína-proteína (PPI). https://doi.org/10.1186/s12870-024-05280-5

# Perguntas de Pesquisa

## Pergunta Principal

- Como o tamanho das partículas de poliestireno (0,1 µm vs 1 µm) influencia os módulos de coexpressão gênica em fibroblastos pulmonares humanos quando comparado em concentrações equivalentes, e quais módulos e hubs estão associados a respostas de estresse celular?

## Perguntas Específicas

- Quais genes são diferencialmente expressos em HPFs expostos a partículas de 100 nm e 1 µm em comparação ao grupo controle?
- Quais módulos de coexpressão gênica se associam com tamanho de partícula e concentração?
- Quais hubs aparecem como candidatos a reguladores centrais da resposta celular?
- Quais processos biológicos e vias moleculares estão enriquecidos nos módulos mais associados às condições experimentais?

## Hipótese

Partículas de 100 nm, por serem internalizadas pelas células, ativam principalmente vias mitocondriais (fosforilação oxidativa) e de síntese proteica — respostas típicas de estresse intracelular. Partículas de 1 µm, por sua afinidade com a membrana celular, comprometem a homeostase proteica (proteostase) e a maquinaria ribossomal — levando ao colapso da tradução. Esperamos, portanto, que os módulos de coexpressão associados ao tamanho de partícula sejam enriquecidos para processos ligados ao ribossomo e à proteostase para exposição a 1 µm, e para OxPhos/metabolismo energético para 100 nm.

# Metodologia

## Bases de Dados

Os dados de RNA-seq foram obtidos do repositório público Gene Expression Omnibus (GEO) sob o número de acesso **GSE296007** (Chwiej et al., 2025). O conjunto consiste em 24 amostras de fibroblastos pulmonares humanos (HPFs) expostos por 24 horas a partículas de poliestireno em diferentes tamanhos e concentrações, com 3 réplicas biológicas por condição:

| Grupo | Tamanho | Concentração | n |
|-------|---------|--------------|---|
| CTR   | —       | 0 g/L        | 3 |
| MA100 | 100 nm  | 0,1 g/L      | 3 |
| MB100 | 100 nm  | 0,01 g/L     | 3 |
| MC100 | 100 nm  | 0,001 g/L    | 3 |
| MA1   | 1 µm    | 0,1 g/L      | 3 |
| MB1   | 1 µm    | 0,01 g/L     | 3 |
| MC1   | 1 µm    | 0,001 g/L    | 3 |
| MD1   | 1 µm    | 0,05 g/L     | 3 |

As anotações funcionais dos genes foram obtidas via **MyGene.info API** (símbolos HGNC a partir de IDs Ensembl) e os termos de enriquecimento funcional foram consultados na base **Enrichr** (GO Biological Process 2023 e KEGG 2021 Human). As interações proteína-proteína foram extraídas do banco **STRING v12** com limiar de alta confiança (combined score ≥ 0,7).

## Modelo Lógico

O modelo lógico do projeto foi desenvolvido na Entrega 1 (project1) e formaliza as entidades principais — amostras, genes, módulos de coexpressão e interações PPI — e seus relacionamentos. O pipeline de análise segue o fluxo:

```
Dados brutos (HTSeq/STAR counts)
    → Filtragem e normalização
    → DESeq2 (genes diferencialmente expressos)
    → WGCNA (módulos de coexpressão)
    → Anotação funcional
    → Exportação para rede PPI (STRING/Cytoscape)
    → Enriquecimento funcional por módulo (ORA)
    → Identificação de genes hub (cytoHubba)
    → Cruzamento hub × enriquecimento
```

## Integração entre Bases

A integração ocorre em dois pontos principais do pipeline:

1. **Genes Ensembl → símbolos HGNC:** Os IDs Ensembl dos arquivos de contagem (HTSeq) foram mapeados para símbolos HGNC via MyGene.info API, permitindo a submissão ao STRING e ao Enrichr, que usam nomenclatura de símbolo.
2. **DEGs + Módulos WGCNA → Rede PPI:** Os 601 genes que são ao mesmo tempo DEGs prioritários (padj < 0,10, |log2FC| ≥ 1,0 em contrastes prioritários) e pertencem a um dos 6 módulos selecionados foram submetidos ao STRING para construção da rede de interação proteína-proteína.

## Análises Realizadas

O pipeline completo compreende oito notebooks executados em sequência:

| Notebook | Análise | Principais saídas |
|----------|---------|-------------------|
| 000 | Estruturação dos dados | Matriz de contagem 63.241 genes × 24 amostras |
| 001 | Controle de qualidade e filtragem | 12.176 genes proteicos filtrados |
| 002 | Expressão diferencial (DESeq2) | 10 contrastes; `deg_all_contrasts.csv` |
| 003 | WGCNA — redes de coexpressão | 29 módulos; correlações módulo-trait |
| 004 | Anotação gênica (MyGene API) | Ensembl → símbolo HGNC (100% mapeados) |
| 005 | Exportação para rede PPI | 601 genes → STRING; sessão Cytoscape |
| 006 | Enriquecimento funcional (ORA) | GO BP e KEGG por módulo via GSEApy/Enrichr |
| 007 | Genes hub — consenso e cruzamento | 10 hubs consensuais × termos enriquecidos |

### Parâmetros-chave

- **DESeq2:** modelo `~ group`; 10 contrastes (7 vs CTR + 3 comparações de tamanho); threshold de DEG: padj < 0,05 e |log2FC| > 1.
- **WGCNA:** rede signed hybrid; poder de soft-thresholding β = 4 (R² = 0,80); `minModuleSize` = 20; `MEDissThreshold` = 0,25; eigengenes calculados por PCA.
- **Seleção de módulos:** padj < 0,10 e |log2FC| ≥ 1,0 em contrastes prioritários; módulo mantido se ≥ 5 DEGs prioritários.
- **Enriquecimento ORA:** background = 12.176 genes medidos; limiar de significância FDR < 0,05.
- **Hub genes:** rede STRING alta confiança (score ≥ 0,7); cytoHubba no Cytoscape com métricas MCC e Degree; consenso = interseção TOP 10 de ambas as métricas.

## Evolução do Projeto

O projeto foi desenvolvido em três entregas:

- **Entrega 1 (project1):** Proposta de projeto, formulação das perguntas de pesquisa e modelo lógico dos dados.
- **Entrega 2 (project2):** Pipeline de pré-processamento (estruturação, QC, filtragem) e análise de expressão diferencial (DESeq2).
- **Entrega 3 (project3-final):** Análise de coexpressão (WGCNA), exportação para rede PPI, enriquecimento funcional e identificação de genes hub. Esta entrega constitui o núcleo original do projeto, avançando além do estudo de referência (Chwiej et al., 2025), que realizou apenas DESeq2 + GO/KEGG simples.

# Ferramentas

| Ferramenta | Uso |
|------------|-----|
| Python 3.11 | Linguagem principal do pipeline |
| PyDESeq2 | Análise de expressão diferencial (implementação Python do DESeq2) |
| PyWGCNA | Análise de coexpressão ponderada (wrapper Python do WGCNA R) |
| GSEApy | Over-Representation Analysis (ORA) via API Enrichr |
| Pandas / NumPy | Manipulação de dados tabulares |
| Plotly | Visualizações interativas |
| Cytoscape 3.x | Visualização e análise topológica de rede PPI |
| STRING v12 | Banco de interações proteína-proteína (alta confiança) |
| cytoHubba | Plugin Cytoscape para identificação de genes hub (MCC, Degree) |
| MyGene.info | API de anotação gênica (Ensembl → HGNC) |
| Enrichr | Base de dados de enriquecimento funcional (GO BP, KEGG) |
| GEO / NCBI | Fonte dos dados brutos (acesso GSE296007) |

# Resultados

## Expressão Diferencial

Após filtragem de qualidade, 12.176 genes proteicos foram retidos. O DESeq2 identificou genes diferencialmente expressos (padj < 0,05, |log2FC| > 1) em 10 contrastes. Os contrastes mais informativos foram:

| Contraste | DEGs |
|-----------|------|
| MC100_vs_MC1 | 1.914 |
| MC1_vs_CTR | 1.481 |
| MA100_vs_CTR | 1.361 |
| MD1_vs_CTR | 1.227 |
| MB1_vs_CTR | 689 |
| MA1_vs_CTR | 238 |
| MB100_vs_CTR | 3 |
| MC100_vs_CTR | 0 |

O contraste de maior impacto transcriptômico foi MC100_vs_MC1 (1.914 DEGs), evidenciando que o efeito diferencial de tamanho é mais pronunciado em baixas concentrações. Em alta concentração (MA100_vs_CTR vs MA1_vs_CTR), as partículas de 100 nm causam ~6× mais DEGs do que as de 1 µm, sugerindo que a dose-resposta é assimétrica entre os dois tamanhos.

## Módulos de Coexpressão (WGCNA)

O WGCNA identificou **29 módulos** de coexpressão. Os três maiores módulos foram: dimgrey (3.883 genes), darkgrey (3.266) e mistyrose (2.130). A correlação módulo-trait mais forte com o tamanho de partícula foi observada para o módulo **darkgrey** (r = +0,622, padj = 0,059), indicando tendência de maior expressão em HPFs expostos a 1 µm. Nenhum módulo atingiu padj < 0,05, o que é esperado dado o baixo n de tratados (n = 21).

**Seis módulos** foram selecionados para análise de rede com base em critérios de densidade de DEGs e relevância biológica: darkgrey (203 DEGs prioritários), dimgrey (302), gainsboro (46), mistyrose (38), indianred (6) e white (6).

## Rede PPI e Enriquecimento Funcional

Os 601 genes que são DEGs prioritários nesses 6 módulos foram submetidos ao STRING (alta confiança, score ≥ 0,7), resultando em **668 interações**. A sessão Cytoscape foi construída com subredes por módulo para análise topológica.

O enriquecimento funcional (ORA, FDR < 0,05) revelou que o módulo **dimgrey** é o único com enriquecimento robusto e biologicamente interpretável:

- **GO Biological Process:** 7 termos significativos, incluindo _Cytoplasmic Translation_ (GO:0002181), _Ribosome Biogenesis_, _rRNA Processing_, _tRNA Aminoacylation_
- **KEGG:** 3 vias significativas, incluindo _Ribosome_ (hsa03010)

Os módulos white (8 genes input) e indianred (6 genes) apresentaram respectivamente 20 e 34 termos GO BP significativos, mas com listas de entrada muito pequenas — esses resultados são considerados exploratórios.

## Genes Hub Consensuais

A análise cytoHubba na rede de alta confiança identificou genes hub pelas métricas MCC e Degree. Os TOP 10 de ambas as métricas foram **idênticos**, resultando em **10 genes hub consensuais**:

| Gene | Função | Módulo | Regulação (1 µm) |
|------|--------|--------|-----------------|
| RPS2 | Proteína ribossomal 40S S2 | dimgrey | Downregulado |
| RPS3 | Proteína ribossomal 40S S3 | dimgrey | Downregulado |
| RPS3A | Proteína ribossomal 40S S3A | dimgrey | Downregulado |
| RPSA | Proteína ribossomal 40S SA | dimgrey | Downregulado |
| RPL3 | Proteína ribossomal 60S L3 | dimgrey | Downregulado |
| RPL7 | Proteína ribossomal 60S L7 | dimgrey | Downregulado |
| RPL26 | Proteína ribossomal 60S L26 | dimgrey | Downregulado |
| RPL31 | Proteína ribossomal 60S L31 | dimgrey | Downregulado |
| RPS23 | Proteína ribossomal 40S S23 | dimgrey | Downregulado |
| RPS27 | Proteína ribossomal 40S S27 | dimgrey | Downregulado |

Todos os 10 genes hub pertencem ao módulo **dimgrey** e são proteínas ribossomais (subunidades 40S e 60S). Todos os 10 estão presentes no overlap do termo GO "Cytoplasmic Translation (GO:0002181)", demonstrando coerência biológica entre a centralidade topológica e a função anotada.

# Discussão

## Colapso da Maquinaria Ribossomal como Resposta Central a 1 µm

O resultado mais consistente deste trabalho é que a exposição a partículas de poliestireno de 1 µm converge, tanto na análise de coexpressão (módulo dimgrey) quanto na topologia da rede PPI (hubs MCC/Degree), para **downregulação de proteínas ribossomais**. Os 10 genes hub consensuais são exclusivamente subunidades das subunidades 40S e 60S do ribossomo citoplásmatico, e todos aparecem no mesmo termo GO de máxima significância: _Cytoplasmic Translation_ (GO:0002181).

Essa convergência confirma e estende os achados de Chwiej et al. (2025), que identificaram por DESeq2 simples a downregulação de RPS2, RPS3A e RPS20 em HPFs expostos a 1 µm. A abordagem de rede revela que esses genes não são regulados isoladamente: eles formam um módulo de coexpressão altamente coeso (dimgrey, 3.883 genes) com forte centralidade na rede de interação proteína-proteína. Isso sugere que a perturbação ribossomal é um **ponto de colapso topológico** da resposta celular, não apenas um artefato de genes individuais.

## Paradoxo de Concentração-Tamanho

O contraste MC100_vs_MC1 (baixa concentração, comparação entre tamanhos) foi o que produziu o maior número de DEGs (1.914), enquanto MA100_vs_CTR (alta concentração, 100 nm) produziu 1.361 DEGs e MA1_vs_CTR (alta concentração, 1 µm) apenas 238. Isso indica que o efeito diferencial de tamanho é mais pronunciado em baixa concentração — concordando com o "paradoxo de concentração" descrito por Chwiej et al., no qual as curvas dose-resposta de 100 nm e 1 µm são inversas.

## Módulos White e Indianred

Os módulos white e indianred (6 genes DEGs cada) produziram numerosos termos significativos no ORA, o que é esperado quando a lista de entrada é muito pequena: com ≤ 10 genes, qualquer coincidência de 2–3 genes em um conjunto gênico tende a ser estatisticamente significativa por ORA. Esses resultados são tratados como exploratórios e não conclusivos.

## Comparação com a Referência Metodológica (Sainz et al., 2024)

O pipeline seguido neste trabalho é análogo ao de Sainz et al. (2024), com duas diferenças metodológicas notáveis:

1. **Identificação de hubs:** Sainz et al. usam conectividade intramodular kWithin (soma dos pesos de correlação dentro do módulo WGCNA). Neste trabalho, foram usadas métricas de centralidade na rede PPI (MCC e Degree via cytoHubba). Ambas as abordagens visam identificar genes centrais; a abordagem PPI tem a vantagem de usar informação biológica independente (interações proteína-proteína validadas em STRING).
2. **Background do ORA:** Foi usado o conjunto dos 12.176 genes medidos (proteicos) como background, não o genoma humano completo — escolha mais conservadora e biologicamente adequada.

## Limitações

- **Baixo n:** Com apenas 21 amostras tratadas (7 grupos × 3 réplicas), o poder estatístico para detectar correlações módulo-trait é limitado. Nenhum módulo atingiu padj < 0,05 para a correlação com particle_size_um.
- **Normalização VST:** O input do WGCNA usou log2(normed+1) em vez de transformação VST verdadeira, o que pode afetar ligeiramente a estrutura dos módulos.
- **Validação funcional:** Os genes hub identificados são candidatos computacionais; validação experimental (knockdown, proteômica) será necessária para estabelecer causalidade.

# Conclusão

Este trabalho demonstrou que a exposição de fibroblastos pulmonares humanos a partículas de poliestireno de 1 µm leva ao colapso coordenado da maquinaria de tradução citoplásmatica. A análise integrada de coexpressão gênica (WGCNA) e rede de interação proteína-proteína (STRING/cytoHubba) identificou o módulo **dimgrey** como o principal módulo resposta, enriquecido para _Cytoplasmic Translation_ e _Ribosome Biogenesis_, com 10 genes hub consensuais — todos proteínas ribossomais das subunidades 40S e 60S: **RPS2, RPS3, RPS3A, RPSA, RPL3, RPL7, RPL26, RPL31, RPS23 e RPS27**.

A identidade entre os TOP 10 hubs das métricas MCC e Degree reforça a robustez desse resultado. Esses genes são os mesmos identificados por Chwiej et al. (2025) como downregulados na análise clássica de genes isolados — a ciência de redes não apenas confirma esse achado, mas o eleva a um fenômeno sistêmico de centralidade topológica.

O projeto avança além do estudo original ao revelar a **hierarquia regulatória da resposta celular**: a perturbação ribossomal não é um conjunto disperso de genes desregulados, mas um colapso coordenado de um módulo topologicamente central. Esse tipo de análise é fundamental para identificar alvos terapêuticos relevantes em doenças respiratórias associadas à exposição a MNPs.

# Trabalhos Futuros

- Validar a identificação de hubs com a métrica kWithin (conectividade intramodular WGCNA), como utilizado em Sainz et al. (2024), e comparar com os hubs MCC/Degree obtidos via PPI.
- Expandir a análise ao módulo **darkgrey**, que apresenta a maior correlação com tamanho de partícula (r = +0,622), para verificar se os hubs de 100 nm seguem padrão complementar ao de 1 µm.
- Aumentar o tamanho amostral com dados de RNA-seq adicionais de HPFs expostos a MNPs para melhorar o poder estatístico das correlações módulo-trait.
- Realizar validação experimental dos genes hub identificados (silenciamento por siRNA, proteômica) para estabelecer relações causais entre centralidade de rede e resposta funcional.
- Integrar dados de microscopia Raman de Chwiej et al. (localização subcelular das partículas) com os módulos WGCNA para relacionar mecanismo de entrada das partículas com o programa transcriptômico ativado.

# Referências Bibliográficas

- Chwiej, J., et al. (2025). _Study on the respiratory toxicity of 0.1 µm and 1 µm polystyrene particles in human lung fibroblasts_. Gene Expression Omnibus, GSE296007. Disponível em: https://doi.org/10.1038/s41598-025-22947-7
- Sainz, M., et al. (2024). _Application of Weighted Gene Co-expression Network Analysis (WGCNA) and Protein-Protein Interaction networks_. BMC Plant Biology. Disponível em: https://doi.org/10.1186/s12870-024-05280-5
- Langfelder, P., & Horvath, S. (2008). _WGCNA: an R package for weighted correlation network analysis_. BMC Bioinformatics, 9(1), 559.
- Love, M. I., Huber, W., & Anders, S. (2014). _Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2_. Genome Biology, 15(12), 550.
- National Center for Biotechnology Information (NCBI). _Sequence Read Archive (SRA), Accession PRJNA868178_.
