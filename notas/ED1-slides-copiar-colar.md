# ED1 — Slides (copiar/colar) · ~4–5 min

Cole cada bloco em um slide. Fonte grande, pouco texto. Fale o que está em *itálico*.

---

## Slide 1 — Capa

**Matrizes e sistemas lineares em imagens digitais**

Álgebra Linear · Ciência da Computação  
**18/09/2026**

*“Boa tarde. Vou mostrar como a imagem digital é tratada com matrizes — no dia a dia do programador.”*

---

## Slide 2 — Como a imagem se organiza (~1 min) ← abrir com isto

**Imagem m×n = 3 matrizes do mesmo tamanho**

Exemplo: foto **20×20** colorida

- matriz **R** 20×20 (vermelho)  
- matriz **G** 20×20 (verde)  
- matriz **B** 20×20 (azul)  

**Mesma posição `(linha, coluna)` nas três = o mesmo pixel.**  
Na tela: R, G e B daquela casa acendem juntos → **1 cor**.

```text
  R 20×20     G 20×20     B 20×20
  [ ... ]  +  [ ... ]  +  [ ... ]  →  imagem na tela
                 ↓
        pixel (i,j) = luz (Rij, Gij, Bij)
```

Recorte real 3×3 (mesmo esquema, só menor):

```
R = |196 184 201|   G = |188 171 189|   B = |177 162 177|
    |110  85  89|       | 85  56  58|       | 80  52  55|
    | 38  33  29|       | 41  39  39|       | 32  29  28|
```

*“Não é uma mistura bagunçada: são 3 tabelas alinhadas. No ponto (1,1), R G e B daquele ponto viram a cor final.”*

---

## Slide 3 — Operações no dia a dia (~1 min)

**O programador percorre a matriz (`img[y][x]`) e aplica operações**

| Álgebra Linear | Na imagem |
|----------------|-----------|
| Transposta `Aᵀ` | Espelha pela diagonal |
| Escalar `kA` | Contraste |

*“Transposta troca linha/coluna. Multiplicar por escalar muda o contraste.”*

---

## Slide 4 — Sistema linear (~1,5–2 min) · exemplo didático

**Ferramenta da disciplina:** várias incógnitas + várias condições.  
*(Imagem pronta para colar: `_ed1_assets/slide04_sistema_gauss_detalhado_wide.png`)*

### Sistema

```
R + G + B = 561
2R + G    = 580
R + 2B    = 550
```

Ampliada `[A|B]`:

```
[ 1  1  1 | 561 ]
[ 2  1  0 | 580 ]
[ 1  0  2 | 550 ]
```

### Gauss (detalhe)

1. `L₂ ← L₂ − 2L₁` → `[0  −1  −2 | −542]`  
2. `L₃ ← L₃ − L₁`  → `[0  −1   1 |  −11]`  
3. `L₃ ← L₃ − L₂`  → `[0   0   3 |  531]` → **B = 531/3 = 177**  
4. Em `L₂`: `−G − 2·177 = −542` → `−G = −188` → **G = 188**  
5. Em `L₁`: `R + 188 + 177 = 561` → **R = 196**

### Conferência

`196+188+177=561` · `2·196+188=580` · `196+2·177=550`

*“Exemplo didático com o método da aula. No dia a dia o arquivo já traz R, G e B separados.”*

---

## Slide 5 — Fechamento (~20 s)

1. Imagem colorida = **3 matrizes alinhadas** (R, G, B)  
2. Operações de matriz = efeitos na imagem  
3. Sistema linear = ferramenta para descobrir valores (exemplo)  

STEINBRUCH; WINTERLE · GONZALEZ; WOODS  

*“Obrigado.”*
