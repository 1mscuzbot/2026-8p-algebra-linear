# ED2 — Roteiro oral (PageRank / autovalores)

**Apresentação:** 06/11 ou 13/11/2026 · **4–5 min**  
**App:** [`index.html`](./index.html) · atalhos `1`–`4` · `→` / `Espaço` · `←`  
**Projetor:** tema claro, **CAIXA ALTA**, palco **4:3**, botão **Tela cheia** ou **F11**.

Alinha às Aulas 10–11 e às notas `notas/ED2-*`.

---

## Pronúncia rápida (não trave no quadro)

| Símbolo / fórmula | Fale assim |
|-------------------|------------|
| **λ** | **lâmbda** (não “lâmbida”) |
| **Av = λv** | “A vê igual a **lâmbda** vê” |
| **Gv = v** | “**Gê vê** igual a **vê**” (G × v = v) |
| **v ← Gv** | “vê recebe **Gê vê**” |
| **λ = 1** | “lâmbda igual a um” |

---

## Exemplos das páginas (etapa 2)

Use os mesmos rótulos da app:

| Página | Exemplo oral |
|--------|----------------|
| **A** | Wikipedia |
| **B** | um blog |
| **C** | portal de notícias |

Links do grafo: **A→B,C** · **B→A,C** · **C→A** (C manda tudo para A → A sobe).

---

## Roteiro por etapa (1–4)

| Tempo | Etapa | Fala |
|------:|-------|------|
| 0:00–0:40 | **1. Ideia** | “No ED1 o pixel era matriz. Aqui: Av = λv — direção que não muda. Aplicação: PageRank.” |
| 0:40–1:40 | **2. Grafo** | “Exemplo: A = Wikipedia, B = blog, C = portal de notícias.” Mostrar G. “Colunas somam 1 → λ = 1. C manda tudo para A.” |
| 1:40–3:40 | **3. Iterar** | 2–3× **1 passo** (ou **Estabilizar**). “v ← Gv: o peso flui pelos links.” Comparar com **4/9**, **2/9**, **1/3**. |
| 3:40–4:40 | **4. Conferir** | “**Gv = v.** Ranking **A > C > B**.” Fechar: autovetor = direção que não muda; PageRank; ranking da web **é** esse vetor (λ = 1). |

Se apertar o tempo: pule a iteração e vá direto à etapa 4 com o vetor exato.

### Números-alvo (folha)

- **A = 4/9** · **C = 1/3** · **B = 2/9**
- Verificação na tela: **Gv = v** (sim) e ranking **A > C > B**

---

## 5 bullets — o que estudar

1. Definição **Av = λv** (Aula 10) e geometria (estica / encolhe / inverte).
2. Passo **(A − λI)v = 0** (Aula 11); no exemplo, **λ = 1**.
3. Matriz G dos links e ranking **A = 4/9 > C = 1/3 > B = 2/9**.
4. Mensagem final: autovetor = direção que não muda; PageRank; ranking da web é esse vetor (λ = 1).
5. Cronometrar a fala com a app aberta (meta ≤ 5 min).

---

## Como abrir

```bash
cd projetos/ed2-autovalores-app
xdg-open index.html
# ou: python3 -m http.server 8765  →  http://127.0.0.1:8765/
```

Sem dependências.

## Arquivos relacionados

| Path | Uso |
|------|-----|
| [`index.html`](./index.html) | App de projeção |
| [`README.md`](./README.md) | Como abrir + resumo |
| [`notas/ED2-aplicacoes-autovalores-pagerank.md`](../../notas/ED2-aplicacoes-autovalores-pagerank.md) | Visão geral ED2 |
| [`notas/ED2-slides-copiar-colar.md`](../../notas/ED2-slides-copiar-colar.md) | 5 slides PPT |
| [`notas/ED2-folha-calculo.md`](../../notas/ED2-folha-calculo.md) | Conta no papel |
| [`material/exercicios/demo-autovalores-pagerank.py`](../../material/exercicios/demo-autovalores-pagerank.py) | Conferência no terminal |
