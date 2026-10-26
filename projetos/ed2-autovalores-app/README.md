# ED2 — App PageRank / autovalores

Demo visual para a apresentação de **4–5 min** (06/11 ou 13/11/2026).  
Alinha às notas [`notas/ED2-aplicacoes-autovalores-pagerank.md`](../../notas/ED2-aplicacoes-autovalores-pagerank.md) e à folha de cálculo.

**Mensagem:** em computação, o autovetor é a direção que não muda; no PageRank, o ranking das páginas **é** o autovetor de λ = 1.

## Como abrir (sem instalar nada)

```bash
cd projetos/ed2-autovalores-app
# Linux / notebook:
xdg-open index.html
# ou abra o arquivo no Chrome/Firefox/Edge
```

Alternativa: servidor local (útil se o navegador bloquear `file://`):

```bash
cd projetos/ed2-autovalores-app
python3 -m http.server 8765
# abra http://127.0.0.1:8765/
```

Atalhos na tela: `1`–`4` etapas · `→` / `Espaço` avança · `←` volta.

## Roteiro oral (~4–5 min)

| Tempo | Etapa na app | O que falar |
|------:|--------------|-------------|
| 0:00–0:40 | **1. Ideia** | “No ED1 o pixel era matriz. Aqui: Av = λv — direção que não muda. Três áreas: busca, imagens/dados, redes.” |
| 0:40–1:40 | **2. Grafo** | Mostrar A/B/C e a matriz G. “Colunas somam 1 → λ = 1. C manda tudo para A.” |
| 1:40–3:40 | **3. Iterar** | Clicar **1 passo** 2–3× (ou **Rodar até estabilizar**). “v ← Gv: o peso flui pelos links.” Comparar com 4/9, 2/9, 1/3. |
| 3:40–4:40 | **4. Conferir** | “Gv = v. Ranking A > C > B. Mesma conta da aula: (G − λI)v = 0.” Fechar com as 3 áreas + Steinbruch. |

Se apertar o tempo: pule a iteração e vá direto à etapa 4 com o vetor exato.

## O que estudar antes

1. Definição Av = λv (Aula 10) e ideia geométrica (estica / encolhe / inverte).
2. Passo (A − λI)v = 0 da Aula 11 — no exemplo, λ = 1.
3. Montar G a partir dos links (folha) e o ranking 4/9, 2/9, 1/3.
4. As três áreas em uma frase cada (busca / PCA-eigenfaces / redes).
5. Cronometrar a fala em voz alta com a app aberta (meta ≤ 5 min).

## Arquivos relacionados

| Arquivo | Uso |
|---------|-----|
| [`notas/ED2-slides-copiar-colar.md`](../../notas/ED2-slides-copiar-colar.md) | 5 slides PPT |
| [`notas/ED2-folha-calculo.md`](../../notas/ED2-folha-calculo.md) | Conta no papel |
| [`material/exercicios/demo-autovalores-pagerank.py`](../../material/exercicios/demo-autovalores-pagerank.py) | Conferência no terminal |
