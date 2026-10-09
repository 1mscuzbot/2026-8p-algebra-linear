# ED2 — Onde a computação usa autovalores e autovetores

**Apresentação:** 06/11 e 13/11/2026 · **Duração alvo: 4–5 minutos**  
**Tema do enunciado:** aplicações de autovalores e autovetores na área do curso

**Mensagem em uma frase:** em computação, o autovetor é a “direção que não muda”; três áreas usam isso — busca, imagens/dados e redes.

No ED1 o objeto era o pixel: a imagem é uma matriz. Aqui o objeto é a direção estável: Av = λv.

---

## Os arquivos

| # | Arquivo | Para quê |
|---|---------|----------|
| 1 | [ED2-slides-copiar-colar.md](ED2-slides-copiar-colar.md) | 5 slides para colar no PowerPoint |
| 2 | [ED2-folha-calculo.md](ED2-folha-calculo.md) | A conta de uma área só (busca / PageRank), para treinar no papel |
| 3 | [demo-autovalores-pagerank.py](../material/exercicios/demo-autovalores-pagerank.py) | Conferir o exemplo da busca |

```bash
cd 2026-8p-algebra-linear/material/exercicios
python3 demo-autovalores-pagerank.py
```

---

## Timing (4–5 min)

| Tempo | Slide | O que fazer |
|------:|-------|-------------|
| 0:00–0:20 | Capa | “Onde a computação usa autovetor” |
| 0:20–1:00 | A ideia | Av = λv: a direção não muda, λ estica ou encolhe |
| 1:00–2:40 | Três áreas | Busca, imagens/dados, redes — uma frase cada |
| 2:40–4:10 | Exemplo | PageRank: 3 páginas → pesos 4/9, 2/9, 1/3 |
| 4:10–4:40 | Fecho | Repetir as 3 áreas + Steinbruch |

Se apertar: encurte a conta e não rode o Python. As três áreas não saem.

---

## As três áreas (o que falar)

| Área em CC | O que é o autovetor na prática |
|------------|--------------------------------|
| **Busca na web** | O peso de cada página. O vetor de pesos é autovetor da matriz de links (PageRank). |
| **Imagens e dados** | O eixo principal de um conjunto de fotos ou de uma tabela. É a base do PCA e do reconhecimento de faces (eigenfaces). |
| **Redes** | A importância de um nó. Quem é ligado a nós importantes também é importante (centralidade de autovetor). |

---

## Exemplo numérico (só a área de busca)

```
A = 4/9 ≈ 44%    C = 1/3 ≈ 33%    B = 2/9 ≈ 22%
```

Gv = v. Detalhe na folha.

---

## Bibliografia

STEINBRUCH, Alfredo; WINTERLE, Paulo. *Álgebra linear*. Rio de Janeiro: Pearson, 2014. Cap. 6.  
BRIN, Sergey; PAGE, Lawrence. *The Anatomy of a Large-Scale Hypertextual Web Search Engine*. 1998.  
TURK, Matthew; PENTLAND, Alex. *Eigenfaces for Recognition*. Journal of Cognitive Neuroscience, 1991.
