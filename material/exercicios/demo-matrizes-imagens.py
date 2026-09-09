"""
ED1 — Demo rápida: matriz ↔ imagem (transposta + contraste).
Roda sem arquivo externo (usa o recorte 3×3 real da abbey.bmp).

Uso:
  python demo-matrizes-imagens.py

Opcional (se tiver uma imagem):
  python demo-matrizes-imagens.py caminho/foto.bmp
"""

from __future__ import annotations

import sys

try:
    import numpy as np
except ImportError:
    print("Instale numpy: pip install numpy")
    sys.exit(1)


# Recorte real abbey.bmp (y=300..302, x=314..316) — R, G, B
R = np.array([[196, 184, 201], [110, 85, 89], [38, 33, 29]], dtype=float)
G = np.array([[188, 171, 189], [85, 56, 58], [41, 39, 39]], dtype=float)
B = np.array([[177, 162, 177], [80, 52, 55], [32, 29, 28]], dtype=float)


def mostrar(titulo: str, m: np.ndarray) -> None:
    print(f"\n=== {titulo} ===")
    print(np.array2string(m.astype(int), separator=" "))


def demo_recorte() -> None:
    mostrar("Canal R (matriz 3x3)", R)
    mostrar("Transposta R^T", R.T)
    mostrar("Contraste 0.5*R", np.clip(0.5 * R, 0, 255))
    mostrar("Contraste 1.5*R", np.clip(1.5 * R, 0, 255))

    # Pixel (0,0): medicoes do sistema da apresentacao
    r, g, b = R[0, 0], G[0, 0], B[0, 0]
    m1 = r + g + b
    m2 = 2 * r + g
    m3 = r + 2 * b
    print("\n=== Sistema no 1o pixel (R,G,B) =", int(r), int(g), int(b), "===")
    print(f"R+G+B   = {m1:.0f}")
    print(f"2R+G    = {m2:.0f}")
    print(f"R+2B    = {m3:.0f}")

    A = np.array([[1.0, 1.0, 1.0], [2.0, 1.0, 0.0], [1.0, 0.0, 2.0]])
    med = np.array([m1, m2, m3])
    sol = np.linalg.solve(A, med)
    print("Solucao A*X=B ->", np.round(sol).astype(int), "(deve ser 196 188 177)")


def demo_arquivo(caminho: str) -> None:
    try:
        from PIL import Image
    except ImportError:
        print("Para abrir arquivo: pip install pillow")
        return

    img = np.array(Image.open(caminho).convert("RGB"))
    h, w, _ = img.shape
    print(f"Imagem {caminho}: ordem {h}×{w} (3 canais)")
    y0, x0 = min(300, h - 3), min(314, w - 3)
    recorte = img[y0 : y0 + 3, x0 : x0 + 3]
    mostrar(f"R no recorte [{y0}:{y0+3}, {x0}:{x0+3}]", recorte[:, :, 0])
    mostrar("Transposta R^T", recorte[:, :, 0].T)
    mostrar("0.5*R", np.clip(0.5 * recorte[:, :, 0], 0, 255))


if __name__ == "__main__":
    print("ED1 Algebra Linear - demo matrizes em imagens (~20 s na tela)")
    demo_recorte()
    if len(sys.argv) > 1:
        demo_arquivo(sys.argv[1])
    print("\nPronto. Na apresentacao: mostre R, R^T e 0.5*R; o sistema fica no quadro/slide.")
