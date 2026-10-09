# ED2 — Folha de cálculo (exemplo da área de busca)

Esta conta ilustra **uma** das três áreas (PageRank). As outras duas — imagens/dados e redes — ficam no slide 3, sem conta.

Matriz de links (colunas somam 1). Ordem: A, B, C.

```
G = |  0   1/2   1 |
    | 1/2   0    0 |
    | 1/2  1/2   0 |
```

λ = 1 porque cada coluna soma 1: quem entra numa página redistribui 100% do peso.

Resolver **(G − I) v = 0**, com v₁ + v₂ + v₃ = 1 e v ≠ 0.

---

## 1. Montar G − I

```
G − I = | -1   1/2   1 |
        | 1/2  -1    0 |
        | 1/2  1/2  -1 |
```

Multiplicar as três linhas por 2 (some o sistema, não muda a solução):

```
| -2   1   2 | |v₁|   |0|
|  1  -2   0 | |v₂| = |0|
|  1   1  -2 | |v₃|   |0|
```

---

## 2. Escalonar

Trocar L₁ com L₂:

```
|  1  -2   0 |
| -2   1   2 |
|  1   1  -2 |
```

L₂ ← L₂ + 2 L₁ · L₃ ← L₃ − L₁:

```
| 1  -2   0 |
| 0  -3   2 |
| 0   3  -2 |
```

L₃ ← L₃ + L₂:

```
| 1  -2  0 |
| 0  -3  2 |
| 0   0  0 |
```

---

## 3. Voltar

Da 2ª linha: −3 v₂ + 2 v₃ = 0 → **v₃ = (3/2) v₂**

Da 1ª linha: v₁ − 2 v₂ = 0 → **v₁ = 2 v₂**

Soma 1:

```
2 v₂ + v₂ + (3/2) v₂ = 1
(9/2) v₂ = 1
v₂ = 2/9
v₁ = 4/9
v₃ = 3/9 = 1/3
```

---

## 4. Conferir Gv = v

```
v = | 4/9 |
    | 2/9 |
    | 1/3 |
```

1ª componente: 0·(4/9) + (1/2)·(2/9) + 1·(1/3) = 1/9 + 3/9 = 4/9  
2ª componente: (1/2)·(4/9) + 0 + 0 = 2/9  
3ª componente: (1/2)·(4/9) + (1/2)·(2/9) + 0 = 2/9 + 1/9 = 3/9 = 1/3

Fecha. Ranking: **A = 4/9 > C = 1/3 > B = 2/9**.
