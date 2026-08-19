# Aula 03 — Inversão de Matrizes

**Disciplina:** Álgebra Linear (Prof.ª Maria Eugênia de Carvalho e Silva)
**Data (plano):** Aulas 05–06 · 14/08 · 1º Bimestre
**Slide:** `material/slides/202485_17036_AL- Aulas.pdf` (páginas 14–17)
**Livro texto:** STEINBRUCH; WINTERLE (cálculos: p. 499)

---

## Resumo

- **A.30 — Matriz inversa** `A⁻¹`: dada A quadrada de ordem n, se existir B quadrada de mesma ordem com **`A·B = B·A = Iₙ`**, B é a inversa de A: `A·A⁻¹ = A⁻¹·A = Iₙ` (só existe para matriz **quadrada**).
- **A.31 — Matriz singular:** matriz quadrada com **`det(A) = 0`**. Ex.: `A = |1 4 7; 2 5 8; 3 6 9|` é singular pois det A = **0** (linhas 2 e 3 = 1ª linha + 1 e + 2 → dependentes) — não tem inversa.
- **A.32 — Matriz não-singular (regular):** matriz quadrada com **`det(A) ≠ 0`**. Ex.: `A = |2 3 1; 5 2 2; 3 1 3|` é não-singular pois det A = 8 − 27 − 1 = **−20 ≠ 0** — tem inversa.
- **Método ensinado em aula — operações elementares:** escrever `[A | Iₙ]` e aplicar operações de linha (trocar linhas, multiplicar por escalar, somar múltiplos de uma linha a outra) até obter `[Iₙ | A⁻¹]`.
- **Propriedades (A.33):** `(A⁻¹)⁻¹ = A`, `(Aᵀ)⁻¹ = (A⁻¹)ᵀ`, `(A·B)⁻¹ = B⁻¹·A⁻¹`; a inversa é **única**; `I⁻¹ = I` (det I = 1). Ex.: `A = |8 5; 3 2|` e `C = |2 −5; −3 8|` → `A·C = I` (C é a inversa de A).
- **A.34 — Operações elementares (base do método de inversão):**
  - **I)** Permutação de duas linhas (ou colunas);
  - **II)** Multiplicação de todos os elementos de uma linha (coluna) por um número real **≠ 0**;
  - **III)** Substituição dos elementos de uma linha (coluna) pela soma deles com os elementos correspondentes de outra linha (coluna) previamente multiplicados por um número real **≠ 0** (o mesmo tipo de operação da propriedade IX dos determinantes).
- **Aplicação:** resolver `A·X = B` ⇒ `X = A⁻¹·B` (ponte para a Aula 04).

## Exemplos resolvidos do slide

**Ex. 1 (págs. 16–17) — Inversão por operações elementares** (método `[A | I] → [I | A⁻¹]`; o exemplo começa na pág. 16 e termina na pág. 17):

```
       2  1  3 | 1  0  0
A =  | 4  2  2 | 0  1  0        (det A = 32 ≠ 0 → inversível)
       2  5  3 | 0  0  1

L₁ ← L₁·(1/2):    1  1/2  3/2 |  1/2  0   0
                   4  2    2   |  0    1   0
                   2  5    3   |  0    0   1

L₂ ← L₂ + L₁·(−4):  1  1/2  3/2 |  1/2  0   0
                     0  0   −4   | −2    1   0
                     2  5    3   |  0    0   1

L₃ ← L₃ + L₁·(−2):  1  1/2  3/2 |  1/2  0   0
                     0  0   −4   | −2    1   0
                     0  4    0   | −1    0   1

L₂ ↔ L₃:             1  1/2  3/2 |  1/2  0   0
                     0  4    0   | −1    0   1
                     0  0   −4   | −2    1   0

L₂ ← L₂·(1/4):       1  1/2  3/2 |  1/2  0    0
                     0  1    0   | −1/4  0    1/4
                     0  0   −4   | −2    1    0

L₃ ← L₃·(−1/4):      1  1/2  3/2 |  1/2  0    0
                     0  1    0   | −1/4  0    1/4
                     0  0    1   |  1/2 −1/4  0

L₁ ← L₁ + L₂·(−1/2): 1  0  3/2 |  5/8   0   −1/8
                     0  1  0   | −1/4   0    1/4
                     0  0  1   |  1/2  −1/4  0

L₁ ← L₁ + L₃·(−3/2): 1  0  0 | −1/8   3/8  −1/8
                     0  1  0 | −1/4   0     1/4
                     0  0  1 |  1/2  −1/4   0
```

**A⁻¹ = `|−1/8  3/8  −1/8; −1/4  0  1/4; 1/2  −1/4  0`**, conferido: A·A⁻¹ = A⁻¹·A = I ✓. (Curiosidade: a pivotagem `L₂ ↔ L₃` foi necessária porque o 2º pivot caiu em 0, já que L₂↔L₃ traz −4.)

## Exercícios / Tarefas

| Origem | O que fazer |
|--------|-------------|
| **Tarefa 3** | Calcular a matriz inversa **conforme o método ensinado em aula** (livro p. 499); alternativa: usar o aplicativo, **mostrando o passo a passo** (sugestão: Symbolab online). Resolvida ✓ → [tarefa-3.md](../material/exercicios/tarefa-3.md) (exercícios 5) B⁻¹, 6) C⁻¹ e 13) L⁻¹, com todas as inversas conferidas por B·B⁻¹ = I) |

---

- Aula anterior → [Aula 02 — Determinantes](aula02-determinantes.md) | Próxima aula → [Aula 04 — Sistemas de equações lineares](aula04-sistemas-de-equacoes-lineares.md)