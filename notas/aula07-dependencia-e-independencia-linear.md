# Aula 07 — Dependência e Independência Linear; Base e Dimensão

**Disciplina:** Álgebra Linear (Prof.ª Maria Eugênia de Carvalho e Silva)
**Data (plano):** Aulas 19–20 · 02/10 · 2º Bimestre
**Slide:** `material/slides/202485_17036_AL- Aulas.pdf` (páginas 30–31)
**Livro texto:** STEINBRUCH; WINTERLE (p. 53; tarefa: p. 90, exercícios 47–48)

---

## Resumo

- Um conjunto de vetores é **LI (linearmente independente)** se **nenhum** vetor for **combinação linear** dos outros.
- **Observações do slide:**
  1. Conjunto **LI** ⇔ nenhum vetor é combinação linear dos demais.
  2. Com **só dois vetores**: será **LD** se um for **múltiplo** do outro.
  3. Conjunto com **apenas o vetor nulo**: é **LD**.
  4. Conjunto com **um único vetor não nulo**: é **LI**.
  5. O **conjunto vazio** é LI (convenção).
  6. Se uma **parte** de A é **LD**, então **A é LD**.
- Método prático: escalonar a matriz cujas linhas (ou colunas) são os vetores; se houver linha nula → **LD**; senão → **LI**.
- **Base:** conjunto LI que **gera** o espaço. **Dimensão:** número de vetores da base.
  - Ex.: ℝ³ tem base canônica `{(1,0,0), (0,1,0), (0,0,1)}` → dim ℝ³ = 3.

## Exercícios / Tarefas

| Origem | O que fazer |
|--------|-------------|
| **Tarefa 7** | Classificar conjuntos do ℝ³ (ex. 47) e do P₂ (ex. 48) em **LI ou LD, JUSTIFICANDO** (por quê/cálculos) — livro p. 90 |
| Respostas fornecidas | 47: a) LI b) LI c) LD d) LD e) LD f) LI g) LD — 48: a) LD b) LI c) LD d) LI (ainda assim, justificar!) |

---

- Aula anterior → [Aula 06 — Espaços vetoriais](aula06-espacos-vetoriais-e-combinacao-linear.md) | Próxima aula → [Aula 08 — Transformações lineares](aula08-transformacoes-lineares.md)