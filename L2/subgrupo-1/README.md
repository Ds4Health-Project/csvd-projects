# Grupo: CVDS

**Integrantes do Subgrupo:**

* Beatriz Nascimento Chaves
* Daniel Yuji Hosomi
* Tábata Barbosa

---

## Informações do Artigo

* **Título:** Differential effects of foodborne and waterborne micro(nano)plastics exposure on fish liver metabolism and gut microbiota community
* **Autores:** Zheng S, Wang W-X
* **Ano:** 2025
* **DOI:** [https://doi.org/10.1016/j.jhazmat.2025.137471](https://doi.org/10.1016/j.jhazmat.2025.137471)

---

# Resumo

**Contexto e Objetivo**
A crescente produção e descarte de plásticos causam o acúmulo de micro e nanoplásticos (MNPs) em ambientes aquáticos, onde são absorvidos pelos peixes via dieta ou respiração branquial. Neste contexto, o estudo investigou as diferenças no perfil de expressão gênica hepática e na microbiota intestinal da tilápia-do-nilo (*Oreochromis niloticus*) com base na via de exposição (dieta vs. água) aos MNPs.

**Metodologia e Ciência de Redes**
O estudo aplicou a Análise de Rede de Coexpressão Gênica Ponderada (WGCNA) para agrupar as respostas hepáticas. O modelo do grafo foi:

* **Vértices:** Genes sequenciados no fígado do peixe e os táxons bacterianos (ASVs) identificados no intestino.
* **Arestas (Conexões):** Nas redes restritas ao fígado, as arestas representam a similaridade de coexpressão entre dois genes. Na rede integrada, as arestas representam a correlação estatística (Spearman) entre a presença de uma bactéria e a expressão de um gene.
* **Pesos:** A espessura e o peso das arestas são determinados pelo valor da correlação estatística.

> ![Modelo Lógico de Grafos 1](/L2/subgrupo-1/images/modelo-grafo.png)

> ![Modelo Lógico de Grafos 2](/L2/subgrupo-1/images/modelo-grafo-artigo.png)

Duas propriedades topológicas dos grafos guiaram a interpretação:

* **Detecção de Comunidades:** Genes com padrões de expressão similares foram agrupados em comunidades, permitindo isolar a via de exposição alimentar da via de exposição aquática.
* **Detecção de Hubs:** Dentro dessas comunidades, a análise topológica identificou os *hubs*, que possuem maiores graus de conectividade e peso estrutural, revelando assim os fatores de transcrição reguladores de todo o distúrbio.

Adicionalmente, a microbiota intestinal foi analisada para compreender os mecanismos de dano hepático mediados pelo eixo intestino-fígado, utilizando escalonamento multidimensional não métrico (NMDS) em nível de variantes de sequência de amplicon (ASVs).

**Principais Descobertas**
A sobreposição das redes provou que diferentes vias de contaminação ativam eixos e respostas biológicas completamente distintas:

* **Exposição via Dieta (Alimento):** Induz distúrbios hepáticos principalmente pela desregulação do ciclo circadiano. O fator de transcrição **thrb** atua como o gene *hub* responsável, cuja expressão é modulada conjuntamente pelos filos bacterianos intestinais *Firmicutes*, *Fusobacteriota*, *Proteobacteria* e *Chloroflexi*.
* **Exposição via Água (Brânquias):** Desencadeia distúrbios metabólicos através de respostas imunológicas e inflamatórias. A rede tem como *hub* regulador o gene **fosl2**, que, por sua vez, é predominantemente modulado pelo filo bacteriano *Firmicutes*.

**Conclusão**
As análises indicaram que a ingestão de partículas pela dieta está relacionada à via do ciclo circadiano, enquanto a exposição pela água desencadeia uma resposta inflamatória primária que afeta o metabolismo, a microbiota intestinal também apresentou diferenças entre as vias de exposição. Assim, o estudo demonstra que diferentes vias de exposição ao plástico geram respostas biológicas distintas e reforça sua relevância para a compreensão dos impactos ambientais desses contaminantes em organismos aquáticos.