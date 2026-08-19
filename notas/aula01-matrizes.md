# Aula 01 — Matrizes

**Disciplina:** Álgebra Linear (Prof.ª Maria Eugênia de Carvalho e Silva)
**Data (plano):** Aulas 01–02 · 31/07 · 1º Bimestre
**Slide:** `material/slides/202485_17036_AL- Aulas.pdf` (páginas 1–6)
**Livro texto:** STEINBRUCH; WINTERLE. *Álgebra linear* (referências do slide: p. 379; atividade em sala e tarefa: p. 393)

---

## Resumo

- **Matriz** é uma tabela retangular de números organizada em **m linhas × n colunas** (ordem `m×n`).
- Elemento genérico: `aᵢⱼ` (linha `i`, coluna `j`).
- **Tipos de matrizes:**
  - linha (1×n) e coluna (m×1)
  - **nula** (todos os elementos iguais a 0)
  - **quadrada** (m = n)
  - **diagonal** (elementos fora da diagonal = 0)
  - **identidade** `Iₙ` (diagonal 1, demais 0)
  - **triangular** superior/inferior
  - **simétrica** (A = Aᵀ) e antissimétrica (A = −Aᵀ)
  - **transposta** `Aᵀ` (linhas ↔ colunas)
- **Operações:**
  - **Adição/subtração:** só entre matrizes de mesma ordem, elemento a elemento.
  - **Multiplicação por escalar:** multiplica todos os elementos.
  - **Multiplicação de matrizes:** `A (m×n) · B (n×p) = C (m×p)` — só definida se o nº de colunas de A = nº de linhas de B; elemento `cᵢⱼ = Σ aᵢₖ·bₖⱼ`.
  - **Multiplicação não é comutativa** em geral (`A·B ≠ B·A`).

## Exercícios / Tarefas

| Origem | O que fazer |
|--------|-------------|
| **Tarefa 1** (`material/exercicios/202485_17234_Algebra Linear-Tarefas.pdf`) | Exercícios de **Matrizes** — livro texto p. 393 |
| Atividade em sala | Exercícios de Matrizes — livro texto p. 393 |
| Slide (pág. 1) | Livro texto p. 379 (leitura/exemplos) |

### Exercício resolvido (slide, pág. 1) — igualdade de matrizes

Dadas as matrizes

```
A = | y+4    2  |      B = | 12    2 |
    | 9     x²+4 |          | 9    53 |
```

calcular `y` e `x` de modo que A = B.

**Resolução (pela definição de igualdade, elemento a elemento):**
- 1ª linha, 1ª coluna: `y + 4 = 12 → y = 8`
- 2ª linha, 2ª coluna: `x² + 4 = 53 → x² = 49 → x = ±7`

**Resposta: y = 8 e x = ±7.**

### Exercícios resolvidos (slide, pág. 2) — adição e combinação linear de matrizes

**Ex. 2)** Calcular A + B, com

```
A = | 2  3   8 |      B = | -3  7  1 |
    |-5  9  -6 |          | -4  2  5 |
    | 7  4  -1 |          |  0  9  4 |

A + B = | -1  10   9 |
        | -9  11  -1 |      (soma elemento a elemento: aᵢⱼ + bᵢⱼ)
        |  7  13   3 |
```

**Ex. 4)** Calcular `3A − 2B + 4C` (D = 3A − 2B + 4C):

```
3A = |  6   9  24 |      −2B = |  6  -14  -2 |      4C = | 28  -32  12 |
     |-15  27 -18 |            |  8   -4 -10 |           | 16  -12   8 |
     | 21  12  -3 |            |  0  -18  -8 |           | 36  -20   4 |

D = | 40  -37  34 |
    |  9   11 -20 |           (Cada passo: multiplica pelo escalar e soma);
    | 57  -26  -7 |
```

> C = | 7  -8  3; 4  -3  2; 9  -5  1 | (obtida de 4C ÷ 4).

### Exercícios resolvidos (slide, pág. 3) — multiplicação de matrizes

**Ex. 5)** Calcular o produto das matrizes A(2×4) · B(4×2):

```
A = | -8   4  -6  1 |     B = | 0   4 |
    |  2  -5   7  3 |         | 2  -2 |
                              | 1  -5 |
                              | 3   8 |

C = A·B = | 5  -2 |         (2×4 · 4×2 → 2×2;
          | 6   7 |           cada cᵢⱼ = Σ aᵢₖ·bₖⱼ)
```

**Ex. 6)** Calcular o produto A·X:

```
A = | 2  3  4 |      X = | x |        C = A·X = | 2x + 3y + 4z |
    | 3  5 -4 |          | y |                  | 3x + 5y − 4z |
    | 4  7 -2 |          | z |                  | 4x + 7y − 2z |
```

Nota do slide: C tem **3 linhas e 1 só coluna** — e cada elemento é uma combinação das variáveis (ex.: 1ª linha de C = `2x + 3y + 4z`).

### Exercício resolvido (slide, pág. 4) — sistema linear na forma matricial A·X = B

"O fato de a matriz C do problema anterior ter 3 linhas e 1 só coluna permite escrever, sob a forma matricial, o sistema":

```
| 2   3  4 |   | x |   | −4  |
| 3   5 −4 | · | y | = | 25  |     ⇒   A·X = B
| 4   7 −2 |   | z |   | 24  |

2x + 3y + 4z = −4
3x + 5y − 4z =  25     (efetuando o produto, voltamos ao sistema)
4x + 7y − 2z =  24
```

### Exercícios resolvidos (slide, pág. 5) — combinação linear e igualdade de matrizes

**Ex. 11)** Calcular `X = 2B − 3A − 6C`, com

```
A = | 2   3   8 |      B = | 5  -7  -9 |      C = | 0  9  8 |
    | 4  -1  -6 |          | 0   4   1 |          | 1  4  6 |

2B = | 10 -14 -18 |      3A = |  6   9  24 |      6C = |  0  54  48 |
     |  0   8   2 |           | 12  -3 -18 |           |  6  24  36 |

X = 2B − 3A − 6C = |  4  -77  -90 |
                    | -18  -13  -16 |
```

**Tarefa (p. 393)** — Calcular os valores de `m` e `n` para que as matrizes sejam iguais:

```
A = | m² − 40   n² + 4 |      B = | 41   13 |
    |      6         3 |          |  6    3 |

m² − 40 = 41 → m² = 81 → m = ±9
n² + 4  = 13 → n² = 9  → n = ±3
```

### Exercício resolvido (slide, pág. 6) — produto de três matrizes (AB)·D

**Ex. 17)** Dadas as matrizes

```
A = |  1  -2 |        B = |  1   3  -5  -7 |       D = |  1   7   3  -8 |
    |  3   1 |            |  6   2  -8   3 |           | -3  -1  -1  -3 |
    |  7  -4 |            |                |           |  4   1   9   0 |
    |  5   9 |            |                |           |  5   3   2  -3 |
```

Calcular `(AB)·D` (há também C = | 2 4; −3 5 | no slide, não usada nesta conta):

```
AB = | -11  -1   11  -13 |      (4×2 · 2×4 = 4×4)
     |   9  11  -23  -18 |
     | -17  13   -3  -61 |
     |  59  33  -97   -8 |

(AB)·D = | -29  -104    41   130 |
         | -206   -25  -227   -51 |
         | -373  -318  -213   280 |
         | -468   259  -745  -547 |
```

---

- Próxima aula → [Aula 02 — Determinantes](aula02-determinantes.md)