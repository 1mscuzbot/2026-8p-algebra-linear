# Aula 03 — Inversão de Matrizes

**Disciplina:** Álgebra Linear (Prof.ª Maria Eugênia de Carvalho e Silva)
**Data (plano):** Aulas 05–06 · 14/08 · 1º Bimestre
**Slide:** `material/slides/202485_17036_AL- Aulas.pdf` (páginas 14–17)
**Livro texto:** STEINBRUCH; WINTERLE (cálculos: p. 499)

---

## Resumo

- **Matriz inversa** `A⁻¹`: matriz tal que `A·A⁻¹ = A⁻¹·A = Iₙ` (só existe para matriz **quadrada**).
- **Condição de existência:** `det(A) ≠ 0` (se `det(A) = 0`, A é **singular** e não tem inversa).
- **Método ensinado em aula — operações elementares:** escrever `[A | Iₙ]` e aplicar operações de linha (trocar linhas, multiplicar por escalar, somar múltiplos de uma linha a outra) até obter `[Iₙ | A⁻¹]`.
- Propriedades: `(A⁻¹)⁻¹ = A`, `(A·B)⁻¹ = B⁻¹·A⁻¹`, `(Aᵀ)⁻¹ = (A⁻¹)ᵀ`.
- **Aplicação:** resolver `A·X = B` ⇒ `X = A⁻¹·B` (ponte para a Aula 04).

## Exercícios / Tarefas

| Origem | O que fazer |
|--------|-------------|
| **Tarefa 3** | Calcular a matriz inversa **conforme o método ensinado em aula** (livro p. 499); alternativa: usar o aplicativo, **mostrando o passo a passo** (sugestão: Symbolab online) |

---

- Aula anterior → [Aula 02 — Determinantes](aula02-determinantes.md) | Próxima aula → [Aula 04 — Sistemas de equações lineares](aula04-sistemas-de-equacoes-lineares.md)