# Aula 05 — Problemas envolvendo Sistemas de Equações Lineares

**Disciplina:** Álgebra Linear (Prof.ª Maria Eugênia de Carvalho e Silva)
**Data (plano):** Aulas 09–10 · 28/08 · 1º Bimestre
**Slide:** `material/slides/202485_17036_AL- Aulas.pdf` (páginas 22–24)
**Livro texto:** STEINBRUCH; WINTERLE — interpretação de problemas

---

## Resumo — como modelar um problema

1. **Identificar as variáveis** (o que se quer descobrir: nº de caixas, preços, quantidades, toneladas…).
2. **Extrair as equações** do enunciado (cada linha do enunciado vira uma equação linear).
3. **Montar a matriz ampliada** `[A | B]` e resolver por operações elementares.
4. **Conferir** a solução nos dados do problema (e verificar coerência: valores inteiros/positivos etc.).

## Exercícios / Tarefas

| Origem | Enunciado |
|--------|-----------|
| **Tarefa 5**, ex. 4 (UEL) | Caixas amarelas/verdes/azuis com capacidades dadas; 12 grandes, 72 médios e 84 pequenos — quantas caixas de cada cor? |
| **Tarefa 5**, ex. 5 (UEPG) | Barracas A, B, C vendendo cachorro-quente, pastel e milho verde; consumos e receitas dados — avaliar as afirmações 01–16 |
| **Tarefa 5**, ex. 6 (ENEM) | Promoção de TV + sofá + estante; sistema de 3 equações e desconto de 5% — múltipla escolha |
| **Tarefa 5**, ex. 11 (UNICAMP) | Lata de 0,5 kg de amendoim/caju/pará com custo de R$ 5,75 e restrição do terço — múltipla escolha |
| **Tarefa 5**, ex. 13 (UFPE) | Fábrica com 3 tipos de aço (A1, A2, A3) e 3 tipos de carro (C1, C2, C3) — total de carros construídos |

### Exemplo resolvido (ex. 4 — UEL)

```
A = caixas amarelas, V = verdes, Az = azuis
2A + 2V + 1Az = 12     (brinquedos grandes)
8A + 20V + 10Az = 72   (médios)
10A + 16V + 14Az = 84  (pequenos)
```

Da 1ª: `Az = 12 − 2A − 2V`. Substituindo na 2ª: `8A + 20V + 10(12 − 2A − 2V) = 72 → −12A = −48 → A = 4`.
Então `Az = 4 − 2V`. Na 3ª: `40 + 16V + 14(4 − 2V) = 84 → −12V = −12 → V = 1` e `Az = 2`.

**Resposta: 4 caixas amarelas, 1 verde e 2 azuis.** (Conferência: grandes `8+2+2=12` ✓; médios `32+20+20=72` ✓; pequenos `40+16+28=84` ✓)

---

- Aula anterior → [Aula 04 — Sistemas de equações lineares](aula04-sistemas-de-equacoes-lineares.md) | Próximas aulas: **apresentações do ED1 (04 e 11/09)** — ver [ED1 — Aplicações de matrizes em imagens](ED1-aplicacoes-matrizes-e-sistemas-em-imagens.md)