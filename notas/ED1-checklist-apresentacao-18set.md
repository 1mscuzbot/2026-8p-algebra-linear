# ED1 — Checklist de apresentação (18/09/2026)

**Duração:** 4–5 min · **Tema:** matrizes e sistemas em imagens digitais

Arquivos prontos (já no repo):

| Arquivo | Uso |
|---------|-----|
| [ED1-slides-copiar-colar.md](ED1-slides-copiar-colar.md) | 5 slides → colar no PowerPoint **hoje à noite** |
| [ED1-folha-sistema.md](ED1-folha-sistema.md) | Treinar o escalonamento 1× no papel |
| [../material/exercicios/demo-matrizes-imagens.py](../material/exercicios/demo-matrizes-imagens.py) | Demo opcional (~20 s) |

```bash
cd /home/1mscuzbot/Git/8p-CC/2026-8p-algebra-linear/material/exercicios
python3 demo-matrizes-imagens.py
```

---

## Timing amanhã

| Tempo | Slide | Fala-chave |
|------:|-------|------------|
| 0:00–0:15 | Capa | “Matrizes e sistemas em imagens digitais — 4 minutos.” |
| 0:15–1:00 | Imagem = matriz | Mostrar o 3×3 R/G/B; claro em cima, escuro embaixo |
| 1:00–2:00 | 2 operações | Só `Aᵀ` (espelha) e `kA` (contraste) — ou rodar o Python |
| 2:00–4:15 | Sistema | Montar AX=B → R=196, G=188, B=177 · conferir 2·196+188=580 |
| 4:15–4:45 | Fecho | 3 bullets + Steinbruch · “Obrigado.” |

Se apertar o tempo: **pule a demo** e fique nos números do slide 3.

---

## Sistema (de cor)

```
R + G + B = 561
2R + G    = 580
R + 2B    = 550
→ R=196, G=188, B=177
```

---

## Não fazer

- Entrar em PDI (OpenGL, amostragem, Marr…)
- Mais de 2 operações de matriz
- Improvisar números diferentes do slide

## Antes de dormir

- [ ] 5 slides no PPT (fonte grande)
- [ ] Resolver o sistema **uma vez** na folha, sem olhar
- [ ] Cronometrar a fala em voz alta (meta ≤ 5 min)
- [ ] (Opcional) Testar o `demo-matrizes-imagens.py`
