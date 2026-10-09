# ED2 — Slides (copiar/colar) · ~4–5 min

Cole cada bloco em um slide. Fonte grande, pouco texto. Fale o que está em *itálico*.

**Apresentação:** 06/11 ou 13/11/2026

---

## Slide 1 — Capa

**Onde a computação usa autovalores e autovetores**

Álgebra Linear · Ciência da Computação  
06/11 e 13/11/2026

*“No ED1, o pixel era uma matriz. Hoje: a direção que não muda é um autovetor — e três áreas da computação usam isso.”*

---

## Slide 2 — A ideia (~40 s)

**Autovetor = direção que a transformação não muda**

```
A v = λ v
```

- v ≠ 0: a direção
- λ: estica (λ > 1), encolhe (0 < λ < 1) ou inverte (λ < 0)

*“A matriz mexe nos outros vetores. Neste, só muda o tamanho.”*

---

## Slide 3 — Três áreas (~1 min 30 s) ← foco

**Onde isso aparece na prática**

| Área | O autovetor é… |
|------|----------------|
| **Busca na web** | o peso de cada página (PageRank) |
| **Imagens e dados** | o eixo principal das fotos (PCA, eigenfaces) |
| **Redes** | a importância de um nó no grafo |

- Busca: página ligada a páginas fortes fica forte  
- Imagens: um rosto vira combinação de poucos “rostos-base”  
- Redes: seguidor de gente influente também sobe no ranking  

*“Não são três contas. São três lugares em que o mesmo Av = λv vira um ranking ou um eixo.”*

---

## Slide 4 — Um exemplo, a busca (~1 min 30 s)

**3 páginas → o autovetor é o ranking**

- A liga para B e C · B liga para A e C · C liga só para A

```
v = (4/9,  2/9,  1/3)
A ≈ 44%   >   C ≈ 33%   >   B ≈ 22%
```

*“C manda tudo para A, então A fica em primeiro. A conta é (G − I)v = 0, a mesma da aula. Gv = v.”*

---

## Slide 5 — Fechamento (~30 s)

**Conclusão**

1. Autovetor = direção que não muda  
2. Busca, imagens/dados e redes usam isso  
3. No exemplo, o ranking da web é esse vetor  

**Bibliografia**  
STEINBRUCH; WINTERLE. *Álgebra linear*. Pearson, 2014.  
BRIN; PAGE. 1998. · TURK; PENTLAND. *Eigenfaces for Recognition*. 1991.

*“Obrigado.”*
