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

# Metodologia

## Bases de Dados

## Modelo Lógico

## Integração entre Bases

## Análises Realizadas

## Evolução do Projeto

# Ferramentas

# Resultados

# Discussão

# Conclusão

# Trabalhos Futuros

# Referências Bibliográficas

- Chwiej, J., et al. (2025). _Study on the respiratory toxicity of 0.1 µm and 1 µm polystyrene particles in human lung fibroblasts_. Gene Expression Omnibus, GSE296007. Disponível em: https://doi.org/10.1038/s41598-025-22947-7
- Sainz, M., et al. (2024). _Application of Weighted Gene Co-expression Network Analysis (WGCNA) and Protein-Protein Interaction networks_. BMC Plant Biology. Disponível em: https://doi.org/10.1186/s12870-024-05280-5
- Langfelder, P., & Horvath, S. (2008). _WGCNA: an R package for weighted correlation network analysis_. BMC Bioinformatics, 9(1), 559.
- Love, M. I., Huber, W., & Anders, S. (2014). _Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2_. Genome Biology, 15(12), 550.
- National Center for Biotechnology Information (NCBI). _Sequence Read Archive (SRA), Accession PRJNA868178_.
