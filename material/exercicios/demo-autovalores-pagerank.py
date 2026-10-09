"""ED2 — PageRank 3x3: o ranking e o autovetor de lambda = 1.

Conferencia da folha notas/ED2-folha-calculo.md.
"""

G = [
    [0.0, 0.5, 1.0],
    [0.5, 0.0, 0.0],
    [0.5, 0.5, 0.0],
]
v = [4 / 9, 2 / 9, 1 / 3]


def matvec(A, x):
    return [sum(A[i][j] * x[j] for j in range(3)) for i in range(3)]


gv = matvec(G, v)
print("Paginas: A, B, C")
print("v      =", [round(x, 4) for x in v])
print("G v    =", [round(x, 4) for x in gv])
print("G v = v?", all(abs(gv[i] - v[i]) < 1e-9 for i in range(3)))
print("soma v =", round(sum(v), 6))
print("ranking: A (4/9) > C (1/3) > B (2/9)")
