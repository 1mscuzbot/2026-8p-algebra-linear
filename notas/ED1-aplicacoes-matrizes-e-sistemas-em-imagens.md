# ED1 — Aplicações de Matrizes e Sistemas de Equações na área do curso (Imagens Digitais)

**Disciplina:** Álgebra Linear (Prof.ª Maria Eugênia de Carvalho e Silva)
**Datas de apresentação:** 04/09 e 11/09/2026 (aulas 11–14 do plano)
**Valor:** Estudo Dirigido vale 10,0 · Peso 3,0 (o ED é a média dos trabalhos apresentados)
**Carga horária mínima do trabalho:** 16 h

---

## Sim, dá para usar o material de "geração de imagens"!

A disciplina **Processamento Digital de Imagens e Computação Gráfica (PDICG)** do mesmo curso tem material diretamente reaproveitável: a **imagem digital é uma matriz** — e as operações de imagem são operações de matrizes. É um caso clássico de "aplicações na área do curso (Ciência da Computação)".

**Fontes do repositório a citar:**
- Notas de estudo de PDICG (já no repo `2026-8p-processamento-digital-de-imagens-e-computacao-grafica/notas/`):
  - [Aula 02.1 — imagem como matriz de pixels e armazenamento](../../2026-8p-processamento-digital-de-imagens-e-computacao-grafica/notas/estudo-aula02-1-imagens-conceitos-e-representacao.md)
  - [Aula 02.2 — operações de imagem por varredura (algoritmos)](../../2026-8p-processamento-digital-de-imagens-e-computacao-grafica/notas/estudo-aula02-2-amostragem-e-quantizacao-na-pratica.md)
  - Aula 03 — conectividade (vizinhança usa índices da matriz) `…/estudo-aula03-vizinhanca-conectividade-e-rotulacao.md`
- Slides: `2026-8p-processamento-digital-de-imagens-e-computacao-grafica/material/slides/PDI26-02-1-Imagens.pdf` e `PDI26-02-2-AmostragemQuantização.pdf`
- Código: projeto OpenGL `2026-8p-processamento-digital-de-imagens-e-computacao-grafica/material/exercicios/PDI-Aula-02-proj/` (funções `ZoomOut`, `Thumbnail`, `ConvertToGrayScale`, `ConvertBlackAndWhite`)

## Roteiro da apresentação (5–10 min)

### 1. Introdução (30 s)
Imagem digital m×n = **matriz m×n** em que cada elemento é um **pixel** com valor de intensidade `f(x,y)`. No RGB são 3 matrizes (R, G, B). → liga com a Aula 01 (matrizes, ordem, tipos).

### 2. Operações com matrizes que viraram operações de imagem (2–3 min)
| Álgebra Linear (aula) | Operação em imagens |
|------------------------|----------------------|
| **Transposta** `Aᵀ` (Aula 01) | girar/espelhar a imagem na diagonal — basta trocar linhas por colunas |
| **Submatriz / limitação da ordem** | `ZoomOut`/`Thumbnail` (redimensionar): pegar 1 pixel a cada `fator` → a nova imagem é uma submatriz amostrada |
| **Combinação linear** (Aula 06) | conversão para tons de cinza: `Y = 0,299R + 0,587G + 0,114B` — é uma combinação linear dos 3 canais → produto de **matriz 1×3 por vetor coluna** `[R G B]ᵀ` |
| **Escalar × matriz** (Aula 01) | ajuste de brilho (somar constante) e contraste (multiplicar por escalar) |
| **Matriz identidade** (Aula 01) | transformação "nula" (não altera a imagem) |

### 3. Sistema de equações lineares em imagens (2 min)
- Modelar sistemas com a forma `A·X = B` (Aula 04): o exemplo clássico é a **recuperação de cor**: se um sensor mede combinações lineares dos canais RGB, cada medição é uma equação e o sistema 3×3 resolve os R, G, B originais.
- O enunciado do **ex. 4 da Tarefa 5** (caixas UEL, já resolvido na [Aula 05](aula05-problemas-com-sistemas-lineares.md)) é um modelo pronto de como apresentar a "montagem do sistema + matriz ampliada + escalonamento".

### 4. Demonstração (2 min)
- Usar as imagens `material/exercicios/Imagens/*.bmp` e mostrar a matriz de um pedaço da imagem (ex.: 8×8) impressa no terminal via `ImageClass` (projeto OpenGL de PDICG).
- Se quiser, uma variação em Python (opcional) para gerar o mesmo efeito: `numpy` com `img[:, ::-1]` (espelho), `img.transpose()` (transposta), `img[::fator, ::fator]` (zoom out).

### 5. Conclusão e bibliografia (30 s)
- Concluir: "matrizes armazenam e transformam imagens; sistemas lineares resolvem dependências entre os canais de cor".
- Bibliografia: STEINBRUCH & WINTERLE (Álgebra Linear), GONZALEZ & WOODS (Processamento de Imagens Digitais), slides das duas disciplinas.

## Checklist de apresentação
- [ ] Definir tamanho da matriz + 1 exemplo pequeno com números reais (ex.: imagem 3×3 → matriz 3×3)
- [ ] Mostrar 2–3 tabelas/figuras (matriz ↔ imagem)
- [ ] Resolver UMA aplicação de sistema passo a passo (estilo Tarefa 5)
- [ ] Rodar um programa OpenGL (ou Python) demonstrando transposta/espelho/zoom
- [ ] Citar as fontes (STEINBRUCH; GONZALEZ & WOODS; slides)

---

- Resumo das aulas → [aula01-matrizes](aula01-matrizes.md) · [aula04-sistemas](aula04-sistemas-de-equacoes-lineares.md) · [aula05-problemas](aula05-problemas-com-sistemas-lineares.md) · [aula06-combinacao-linear](aula06-espacos-vetoriais-e-combinacao-linear.md)