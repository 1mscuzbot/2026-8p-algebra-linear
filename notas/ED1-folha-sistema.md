# Folha de treino — sistema do ED1 (sem olhar o gabarito)

Treine **2 vezes** no papel. Meta: resolver em **~90 s**.

---

## Enunciado (o que vai no quadro)

Um sensor mede combinações lineares dos canais de um pixel:

```
R + G + B = 561
2R + G    = 580
R + 2B    = 550
```

Resolva por operações elementares e ache R, G, B.

---

## Espaço para resolver

```
[ A | B ] =

(



)

L₂ ← …
L₃ ← …
…


R = ____    G = ____    B = ____
```

Conferência: `2R + G = ____` (deve ser 580) · `R + 2B = ____` (deve ser 550)

---

## Gabarito (vire só depois)

Ampliada inicial:

```
[ 1  1  1  | 561 ]
[ 2  1  0  | 580 ]
[ 1  0  2  | 550 ]
```

1. `L₂ ← L₂ − 2L₁` → `[ 0  −1  −2 | −542 ]`
2. `L₃ ← L₃ − L₁`  → `[ 0  −1   1 |  −11 ]`
3. `L₃ ← L₃ − L₂`  → `[ 0   0   3 |  531 ]` → ÷3 → **B = 177**
4. Em `L₂`: `−G − 2·177 = −542` → `−G − 354 = −542` → **G = 188**
5. Em `L₁`: `R + 188 + 177 = 561` → **R = 196**

Conferência: `2·196 + 188 = 580` ✓ · `196 + 2·177 = 550` ✓
