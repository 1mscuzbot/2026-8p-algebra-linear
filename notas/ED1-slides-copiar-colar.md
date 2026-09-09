# ED1 — Slides (copiar/colar) · ~4–5 min

Cole cada bloco em um slide. Fonte grande, pouco texto. Fale o que está em *itálico*.

---

## Slide 1 — Capa

**Matrizes e sistemas lineares em imagens digitais**

Álgebra Linear · Ciência da Computação  
11/09/2026

*“Boa tarde. Vou mostrar em 4 minutos como matrizes e sistemas lineares aparecem em imagens digitais.”*

---

## Slide 2 — Imagem = matriz (~45 s)

**Imagem digital = matriz**

- Tons de cinza → 1 matriz `m×n`
- RGB → 3 matrizes (R, G, B)
- Cada número = 1 pixel (0–255)

```
R = |196 184 201|     G = |188 171 189|     B = |177 162 177|
    |110  85  89|         | 85  56  58|         | 80  52  55|
    | 38  33  29|         | 41  39  39|         | 32  29  28|
```

*“Recorte real 3×3: claro em cima, escuro embaixo — a matriz guarda a imagem.”*

---

## Slide 3 — Duas operações (~1 min)

**Operações de matriz → efeito visual**

| Álgebra Linear | Imagem |
|----------------|--------|
| Transposta `Aᵀ` | Espelha pela diagonal (linhas ↔ colunas) |
| Escalar `kA` | Contraste (`k=0,5` ou `k=1,5`) |

```
Rᵀ = |196 110  38|      0,5·R ≈ |98 92 100|
     |184  85  33|               |55 42  44|
     |201  89  29|               |19 16  14|
```

*“Transposta troca linha/coluna. Multiplicar por escalar muda o contraste.”*

---

## Slide 4 — Sistema linear (~2 min) ← foco

**Recuperar R, G, B a partir de medições misturadas**

```
R + G + B = 561
2R + G    = 580
R + 2B    = 550
```

```
| 1  1  1 | |R|   |561|
| 2  1  0 | |G| = |580|
| 1  0  2 | |B|   |550|
```

**Resolução (resumo no slide; detalhe na folha):**

1. `L₂ ← L₂ − 2L₁` · `L₃ ← L₃ − L₁`
2. `L₃ ← L₃ − L₂` → **B = 177**
3. Volta: **G = 188**, **R = 196**

*“É o mesmo método da Tarefa 5: montar `A X = B` e escalonar. Conferência: 2·196+188=580 ✓”*

---

## Slide 5 — Fechamento (~30 s)

**Conclusão**

1. Imagem = matriz  
2. Operações de matriz transformam a imagem  
3. Sistemas lineares recuperam os canais de cor  

**Bibliografia**  
STEINBRUCH; WINTERLE. *Álgebra linear*. Pearson, 2014.  
GONZALEZ; WOODS. *Processamento digital de imagens*.

*“Obrigado.”*
