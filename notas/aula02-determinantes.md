# Aula 02 — Determinantes

**Disciplina:** Álgebra Linear (Prof.ª Maria Eugênia de Carvalho e Silva)
**Data (plano):** Aulas 03–04 · 07/08 · 1º Bimestre
**Slide:** `material/slides/202485_17036_AL- Aulas.pdf` (páginas 7–13)
**Livro texto:** STEINBRUCH; WINTERLE (cálculos: p. 499)

---

## Resumo

- **Determinante** é um número associado a uma matriz **quadrada** `det(A)` ou `|A|`.
- **Ordem 2:** `|a b; c d| = ad − bc`.
- **Ordem 3 (Regra de Sarrus):** repetem-se as duas primeiras colunas à direita; soma dos produtos das 3 diagonais principais menos a soma dos produtos das 3 diagonais secundárias.
- **Desenvolvimento por linha ou coluna (A.26):** o determinante é a soma dos cofatores de uma linha/coluna. A **alternância dos sinais** do cofator `Cᵢⱼ = (−1)^(i+j)·Mᵢⱼ` segue o padrão:

```
+  −  +  −
−  +  −  +
+  −  +  −
−  +  −  +
```

- **Propriedades (A.27):**
  - **I)** O determinante **não se altera** quando se trocam linhas por colunas: `det(Aᵀ) = det(A)`.
    - Ex.: `|2 5; 7 3| = 2·3 − 5·7 = −29` e `|2 7; 5 3| = 2·3 − 7·5 = −29`.
  - **II)** Se A possui **linha (ou coluna) de elementos nulos**, o determinante é **nulo**.
    - Ex.: `A = | 0 0 0; 5 4 1; 3 2 7 |` — expandindo pela 1ª linha: `0·x − 0·x + 0·x = 0`.
  - **III)** Se A tem **duas linhas (ou colunas) iguais**, o determinante é **nulo**.
    - Ex.: `A = | 5 5 2; 3 3 1; 4 4 6 |` (1ª coluna = 2ª coluna).
  - **IV)** Se **duas linhas (ou colunas) têm elementos correspondentes proporcionais**, o determinante é **nulo** (elementos correspondentes: mesma coluna em linhas diferentes, ou mesma linha em colunas diferentes).
    - Ex.: `|2 6; 3 9| = 2·9 − 6·3 = 18 − 18 = 0` (linhas proporcionais: [2,6] = [3,9]·2/3… [2,6] e [3,9] são ×1,5).
  - **V)** Se **cada elemento de uma linha (ou coluna) é soma de duas parcelas**, o determinante se escreve como **soma de dois determinantes**:

```
| a₁   b₁ + c₁ |     | a₁  b₁ |     | a₁  c₁ |
| a₂   b₂ + c₂ |  =  | a₂  b₂ |  +  | a₂  c₂ |
```

  - **Exemplo (pág. 11):** `|2 3+5; 7 4+6| = |2 8; 7 10|` = 2×10 − 8×7 = −36; e `|2 3; 7 4| = −13`, `|2 5; 7 6| = −23`; logo `−13 + (−23) = −36` ✓.
  - **VI)** O determinante de uma matriz **diagonal A (superior ou inferior)** — no jargão usual, **triangular** superior/inferior (a diagonal é o caso particular em que os dois triângulos são nulos) — é igual ao **produto dos elementos da diagonal principal**. Ex.: det de `|3 0 0; 5 1 0; −2 4 2|` = 3·1·2 = 6 (generalização: `det = a₁₁·a₂₂·…·aₙₙ`).
  - **VII)** Trocando-se **duas linhas (ou colunas)** entre si, o determinante **muda de sinal** (fica multiplicado por **−1**).
    - Ex.: `det A = |1 3 5; 0 0 2; 0 4 12| = −8`; trocando a 2ª pela 3ª linha: `det A₁ = |1 3 5; 0 4 12; 0 0 2| = +8` (−1 × −8 ✓).
  - **VIII)** Multiplicar **todos os elementos de uma linha (ou coluna)** por um número real `k` multiplica o determinante por `k`:

```
| a₁   b₁   c₁ |          | a₁   b₁   c₁ |
| k·a₂ k·b₂ k·c₂ |   =  k·| a₂   b₂   c₂ |
| a₃   b₃   c₃ |          | a₃   b₃   c₃ |
```

  - **IX)** O determinante **não se altera** somando-se a uma linha (coluna) os elementos correspondentes de outra linha (coluna) **multiplicados por um número real diferente de zero**:

```
| a₁   b₁   c₁ |          | a₁          b₁              c₁          |
| a₂   b₂   c₂ |    =     | a₂ + k·a₁   b₂ + k·b₁    c₂ + k·c₁   |   (k ≠ 0)
| a₃   b₃   c₃ |          | a₃          b₃              c₃          |
```

  - `det(A·B) = det(A)·det(B)`
- **Significado:** `det(A) ≠ 0` ⇔ A é **inversível** (base para a Aula 03) e é o critério usado em sistemas lineares (Aula 04).

## Exemplos resolvidos do slide

**Ex. 1 (pág. 7)** — `A = | 7 5; 2 4 |` → det A = 7×4 − 2×5 = 28 − 10 = **18**

**Ex. 2 (pág. 7)** — `A = | −3 −8; −5 −2 |` → det A = (−3)·(−2) − (−8)·(−5) = 6 − 40 = **−34**

**A.25 (pág. 8, Sarrus)** — `A = | 3 1 −2; −5 4 −6; 0 2 7 |`:

```
            3   1  -2 | 3   1     (repete 1ª e 2ª coluna)
           -5   4  -6 |-5   4
            0   2   7 | 0   2

det A = 3·4·7 + 1·(−6)·0 + (−2)·(−5)·2  −  [ (−2)·4·0 + 3·(−6)·2 + 1·(−5)·7 ]
      = 84 + 0 + 20 − [ 0 − 36 − 35 ]
      = 84 + 0 + 20 − 0 + 36 + 35 = 175
```

**Pág. 9** — desenvolvimento pela 1ª linha de uma matriz 4×4 (matriz do slide a confirmar: `| 3 4 1 4; 0 1 9 8; 5 6 6 7; 3 1 4 6 |`, calculado = 336) — *pendente de conferência no slide.*

**Pág. 13 (Atividade em sala)** — Calcular det A pela 2ª linha:

```
        |-2  3   1  -1|
        | 0   1   2   3|
   A =  | 1  -1   1  -2|
        | 4  -3   5   1|
```

Expansão pela 2ª linha (sinais −, +, −, +; a₂₁ = 0, não contribui):

- **C₂₂** (+): menor `|−2 1 −1; 1 1 −2; 4 5 1|` = −22 − 9 − 1 = **−32**
- **C₂₃** (−): menor `|−2 3 −1; 1 −1 −2; 4 −3 1|` = 14 − 27 − 1 = **−14**
- **C₂₄** (+): menor `|−2 3 1; 1 −1 1; 4 −3 5|` = 4 − 3 + 1 = **+2**

**det A = 1·(−32) − 2·(−14) + 3·(2) = −32 + 28 + 6 = 2**

## Exercícios / Tarefas

| Origem | O que fazer |
|--------|-------------|
| **Tarefa 2** | Calcular o determinante **pelo aplicativo Symbolab** e **explicar qual método** o aplicativo utilizou (cálculos do livro, p. 499) |

---

- Aula anterior → [Aula 01 — Matrizes](aula01-matrizes.md) | Próxima aula → [Aula 03 — Inversão de matrizes](aula03-inversao-de-matrizes.md)