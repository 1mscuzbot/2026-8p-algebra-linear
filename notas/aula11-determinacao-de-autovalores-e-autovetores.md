# Aula 11 — Determinação de Autovalores e Autovetores

**Disciplina:** Álgebra Linear (Prof.ª Maria Eugênia de Carvalho e Silva)
**Data (plano):** Aulas 27–28 · 30/10 · 2º Bimestre
**Slide:** `material/slides/202485_17036_AL- Aulas.pdf` (páginas 44–47)
**Livro texto:** STEINBRUCH; WINTERLE (slides: p. 279; tarefa: p. 314)

---

## Resumo — passo a passo

Com o operador representado pela matriz `A` (T(v) = A·v):

1. Escrever o sistema homogêneo: `A·v = λ·v ⇔ (A − λI)·v = 0`.
2. **Equação característica:** `det(A − λI) = 0` — resolver para obter os **autovalores** `λ₁, λ₂, …`.
3. Para **cada** `λᵢ`, substituir em `(A − λᵢI)·v = 0` e resolver o sistema (escalonar).
4. O espaço solução (não nulo) dá os **autovetores** associados (autoespaço): `E(λ) = N(A − λI)`.
5. Dica: se `v` é autovetor, **qualquer múltiplo** `αv` também é.

Lembrando (do slide): autovalores podem repetir **multiplicidade**; autovetores de autovalores distintos são **LI**.

## Exercícios / Tarefas

| Origem | O que fazer |
|--------|-------------|
| **Tarefa 11** | Determinar valores próprios e vetores próprios — **fazer passo a passo!!!** (p. 314 do livro texto) |
| Slide (pág. 44) | Continuação — p. 279 do livro texto |

---

- Aula anterior → [Aula 10 — Autovalores e autovetores](aula10-autovalores-e-autovetores.md) | Próxima aula → [Aula 12 — Propriedades dos autovalores](aula12-propriedades-dos-autovalores.md)