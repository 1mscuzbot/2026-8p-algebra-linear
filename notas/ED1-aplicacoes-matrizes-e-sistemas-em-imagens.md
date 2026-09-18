# ED1 — Matrizes e sistemas lineares em imagens digitais

**Apresentação:** 18/09/2026 · **Duração alvo: 4–5 minutos**  
**Tema:** Matrizes e sistemas na área do curso (imagens digitais / Ciência da Computação)

**Mensagem em uma frase:** a imagem digital é uma matriz; operações de matriz a transformam; um sistema linear recupera R, G, B.

**Roteiro de amanhã:** [ED1-checklist-apresentacao-18set.md](ED1-checklist-apresentacao-18set.md)

---

## Os 3 arquivos da apresentação

| # | Arquivo | Para quê |
|---|---------|----------|
| 1 | [ED1-folha-sistema.md](ED1-folha-sistema.md) | Treinar o sistema no papel (~90 s) |
| 2 | [ED1-slides-copiar-colar.md](ED1-slides-copiar-colar.md) | 5 slides prontos para colar no PowerPoint |
| 3 | [demo-matrizes-imagens.py](../material/exercicios/demo-matrizes-imagens.py) | Demo de 20 s (transposta + contraste) |

```bash
cd 2026-8p-algebra-linear/material/exercicios
python demo-matrizes-imagens.py
```

---

## Timing (4–5 min)

| Tempo | Slide | O que fazer |
|------:|-------|-------------|
| 0:00–0:15 | Capa | Título + “imagens = aplicação de AL em Computação” |
| 0:15–1:00 | Imagem = matriz | Mostrar o 3×3; claro/escuro |
| 1:00–2:00 | 2 operações | Só `Aᵀ` e `kA` (ou rodar o Python) |
| 2:00–4:15 | Sistema | Montar `AX=B`, escalonar, chegar em 196, 188, 177 |
| 4:15–4:45 | Fechamento | 3 bullets + Steinbruch |

Se apertar: pule a demo ao vivo e deixe só os números do slide 3.

---

## Sistema (números oficiais)

```
R + G + B = 561
2R + G    = 580
R + 2B    = 550
→ R=196, G=188, B=177
```

---

## Evitar na fala

- Aula de PDI (OpenGL, amostragem, Marr…)
- “Identidade = nula”
- Mais de 2 operações de matriz

---

## Bibliografia

STEINBRUCH; WINTERLE. *Álgebra linear*. Pearson, 2014.  
GONZALEZ; WOODS. *Processamento digital de imagens* (apoio).
