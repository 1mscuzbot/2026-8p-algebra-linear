# Tarefa 3 — Matriz Inversa (pelo método ensinado em aula)

**Disciplina:** Álgebra Linear — Prof.ª Maria Eugênia de Carvalho e Silva
**Conteúdo:** Determinantes / Inversão de matrizes (livro texto, p. 499)
**Enunciado (PDF de tarefas, pág. 4):** calcular as matrizes inversas conforme o método ensinado em aula (ou via aplicativo, mostrando o passo a passo — sugestão: Symbolab online). Exercícios 5), 6) e 13):

```
            -3   4  -5
      B =  | 0   1   2 |
             3  -5   4

             1  0  0  0
             2  1  0  0
      C =  | 3  2  1  0 |        (triangular inferior, diagonal = 1)
             4  3  2  1

            -3  -1  -3
      L =  | 2  -4  -1 |
            -1  -2  -2
```

---

## Exercício 5) — B⁻¹ (desenvolvido passo a passo)

### Passo 0 — Por que a inversa existe?

```
det B = −3·(1·4 − 2·(−5)) − 4·(0·4 − 2·3) + (−5)·(0·(−5) − 1·3)
      = −3·14 − 4·(−6) + (−5)·(−3)
      = −42 + 24 + 15 = −3 ≠ 0   →  B tem inversa ✓
```

### Passo 1 — Ampliada `[B | I]`

Toda operação aplicada à esquerda também vale à direita, até a esquerda virar `I`.

```
[ −3   4  −5  |  1   0   0 ]
[  0   1   2  |  0   1   0 ]
[  3  −5   4  |  0   0   1 ]
```

### Passo 2 — Pivot da 1ª linha = 1

**L₁ ← L₁·(−1/3)**:

```
[  1 −4/3 5/3  | −1/3   0   0 ]
[  0   1   2   |   0    1   0 ]
[  3  −5   4   |   0    0   1 ]
```

### Passo 3 — Zerar abaixo do 1º pivot

**L₃ ← L₃ + L₁·(−3)**: L₃ = `[0, −1, −1 | 1, 0, 1]`

```
[  1 −4/3  5/3  | −1/3  0   0 ]
[  0   1    2   |   0   1   0 ]
[  0  −1   −1   |   1   0   1 ]
```

### Passo 4 — Zerar abaixo do 2º pivot

**L₃ ← L₃ + L₂·(1)**: L₃ = `[0, 0, 1 | 1, 1, 1]`

```
[  1 −4/3 5/3  |−1/3  0   0 ]
[  0   1   2   |  0   1   0 ]
[  0   0   1   |  1   1   1 ]
```

### Passo 5 — Zerar acima da diagonal (subida)

**L₂ ← L₂ + L₃·(−2)**: L₂ = `[0, 1, 0 | −2, −1, −2]`

**L₁ ← L₁ + L₂·(4/3)**: L₁ = `[1, 0, 5/3 | −1/3−8/3, 4/3, −8/3]` = `[1, 0, 5/3 | −3, 4/3, −8/3]`

**L₁ ← L₁ + L₃·(−5/3)**: L₁ = `[1, 0, 0 | −3−5/3, 4/3−5/3, −8/3−5/3]`

```
[  1   0   0  | −14/3  −3  −13/3 ]
[  0   1   0  |  −2    −1   −2   ]
[  0   0   1  |   1     1    1   ]
```

### Resultado e conferência

**B⁻¹ = `[−14/3 −3 −13/3; −2 −1 −2; 1 1 1]`** ✓ (B·B⁻¹ = B⁻¹·B = I₃, verificado por script)

---

## Exercício 6) — C⁻¹ (triangular inferior)

### Passo 0 — `det C = 1·1·1·1 = 1 ≠ 0` → inversível ✓

A triangular inferior, quando invertível, tem inversa **também triangular inferior** — dá para zerar de cima para baixo (subida). Ampliada `[C | I]` e operações:

```
[ 1  0  0  0 |  1  0  0  0 ]
[ 2  1  0  0 |  0  1  0  0 ]
[ 3  2  1  0 |  0  0  1  0 ]
[ 4  3  2  1 |  0  0  0  1 ]

L₂ ← L₂ + L₁·(−2):  [ 0  1  0  0 | −2  1  0  0 ]
L₃ ← L₃ + L₁·(−3):  [ 0  2  1  0 | −3  0  1  0 ]
L₄ ← L₄ + L₁·(−4):  [ 0  3  2  1 | −4  0  0  1 ]

L₃ ← L₃ + L₂·(−2):  [ 0  0  1  0 |  1  −2  1  0 ]
L₄ ← L₄ + L₂·(−3):  [ 0  0  2  1 |  2  −3  0  1 ]

L₄ ← L₄ + L₃·(−2):  [ 0  0  0  1 |  0   1 −2  1 ]
```

### Resultado e conferência

**C⁻¹ = `[1 0 0 0; −2 1 0 0; 1 −2 1 0; 0 1 −2 1]`** ✓ (C·C⁻¹ = I₄, verificado)

Obs.: repare no padrão — os números (2, 3, 4) da subdiagonal viram os coeficientes com sinal alternado (−2, +1, 0 …).

---

## Exercício 13) — L⁻¹

### Passo 0 — `det L`:

```
det L = −3·((−4)·(−2) − (−1)·(−2)) + 1·(2·(−2) − (−1)·(−1)) − 3·(2·(−2) − (−4)·(−1))
      = −3·(8 − 2) + 1·(−4 − 1) − 3·(−4 − 4)
      = −18 − 5 + 24 = 1 ≠ 0   →  L tem inversa ✓
```

### Resolução (ampliada `[L | I]` → operações de linha → `[I | L⁻¹]`)

Resultado conferido por script (frações exatas):

**L⁻¹ = `[6 4 −11; 5 3 −9; −8 −5 14]`** ✓ (L·L⁻¹ = L⁻¹·L = I₃)

Para a entrega: faça o passo a passo completo como no exercício 5) (ficam ~6 operações de linha: 3 para zerar abaixo da diagonal + 3 na subida), ou use o Symbolab e anexe o passo a passo — como exigido no enunciado.

---

## Dica para o aplicativo (Symbolab)

No Symbolab: `Matrix Inverse Calculator` → digite a matriz → o site mostra o processo completo de operações de linha. Use-o desde que **anexe o passo a passo** (print ou transcrição) e **confira com B·B⁻¹ = I**.
