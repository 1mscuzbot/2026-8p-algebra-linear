# Álgebra Linear

**Universidade Tuiuti do Paraná — FACET**
**Professor(a):** Maria Eugênia de Carvalho e Silva
**Carga horária:** 40h | **Período:** 3º ou 4º | **Regime:** Semestral
**Livro texto:** STEINBRUCH, Alfredo; WINTERLE, Paulo. *Álgebra linear*. Pearson, 2014.

> **Branch principal:** `master` (equivalente ao *main* no GitHub).  
> **Atualizado:** 22/10/2026 — panorama abaixo alinha **plano oficial**, **notas no repo** (Aulas 01–12) e **provinhas** (padrão real observado).

## Panorama geral

### Onde estamos (22/10/2026)

| | |
|---|---|
| **Hoje 22/10 → amanhã 23/10** | **Provinha 9** — propriedades das TLs (combinação linear / T definida pela base; Tarefa 9) → [revisão](notas/revisao-provinha-9-23out-propriedades-tl.md) |
| **Mesmo dia 23/10 (plano)** | Aula **10** — operadores / autovalores (intro) — [Aula 10](notas/aula10-autovalores-e-autovetores.md) |
| **Já feita 16/10** | **Provinha 8** — verificar linearidade + T(0) → [revisão](notas/revisao-provinha-8-16out-transformacoes-lineares.md) |
| **Prova bimestral** | 27/11 (2º bimestre) |

**Padrão das provinhas:** aula do conteúdo numa sexta → **provinha** desse conteúdo na **sexta seguinte**, enquanto a professora já avança o próximo tópico.

### Mapa — plano de aulas (título + data)

Cada linha é o **título do plano** (`material/2026727_133027_Algebra Linear-Plano de aula-2026-2.pdf`). Onde existe, a coluna **Nota** aponta o resumo no repo (Aula 01–12).

#### 1º bimestre

| Aulas | Data | Título (conteúdo) | Nota |
|-------|------|-------------------|------|
| 01–02 | 31/07 | Matrizes: definição, tipos e operações | [Aula 01](notas/aula01-matrizes.md) |
| 03–04 | 07/08 | Determinantes | [Aula 02](notas/aula02-determinantes.md) |
| 05–06 | 14/08 | Inversão de matrizes | [Aula 03](notas/aula03-inversao-de-matrizes.md) |
| 07–08 | 21/08 | Sistemas de equações lineares | [Aula 04](notas/aula04-sistemas-de-equacoes-lineares.md) |
| 09–10 | 28/08 | Problemas com sistemas lineares | [Aula 05](notas/aula05-problemas-com-sistemas-lineares.md) |
| 11–12 | 04/09 | Apresentação ED1 (matrizes e sistemas) | [ED1](notas/ED1-aplicacoes-matrizes-e-sistemas-em-imagens.md) |
| 13–14 | 11/09 | Apresentação ED1 | [ED1 checklist](notas/ED1-checklist-apresentacao-18set.md) |
| 15 | 18/09 | Estudo Dirigido 1 + **Avaliação 1º bimestre** | — |

#### 2º bimestre

| Aulas | Data | Título (conteúdo) | Nota / provinha |
|-------|------|-------------------|-----------------|
| 17–18 | 25/09 | Espaços vetoriais; combinação linear | [Aula 06](notas/aula06-espacos-vetoriais-e-combinacao-linear.md) |
| 19–20 | 02/10 | Dependência/independência linear; base e dimensão | [Aula 07](notas/aula07-dependencia-e-independencia-linear.md) *(parte de TL adiantada)* |
| 21–22 | 09/10 | Transformações lineares (núcleo e imagem) | [Aula 08](notas/aula08-transformacoes-lineares.md) · aula real 09/10 (caderno T(0)) |
| 23–24 | **16/10** | Propriedade da transformação linear | [Aula 09](notas/aula09-propriedade-das-transformacoes-lineares.md) · **Provinha 8** no mesmo dia |
| 25–26 | 23/10 | Operadores lineares; autovalores e autovetores (intro) | [Aula 10](notas/aula10-autovalores-e-autovetores.md) · **Provinha 9** *(estimada)* |
| 27–28 | 30/10 | Autovalores/autovetores + estudo dirigido | [Aula 11](notas/aula11-determinacao-de-autovalores-e-autovetores.md) |
| 29–30 | 06/11 | Apresentação ED2 (autovalores) | [ED2](notas/ED2-aplicacoes-autovalores-pagerank.md) |
| 31–32 | 13/11 | Apresentação ED2 | [ED2 slides](notas/ED2-slides-copiar-colar.md) |
| 33–34 | 20/11 | Estudo Dirigido 2 | [Aula 12](notas/aula12-propriedades-dos-autovalores.md) *(plano: repor)* |
| 35–36 | 27/11 | **Avaliação 2º bimestre** | — |
| 37–38 | 03/12 | Revisão | — |
| 39–40 | 04/12 | **Exame final** (2ª chamada 11/12) | — |

### Tarefas ↔ aulas (Steinbruch)

| Tarefa | Título | Livro (ref.) | Ligada à aula |
|--------|--------|--------------|---------------|
| 1 | Matrizes | p. 393 | 01 |
| 2 | Determinantes | — | 02 |
| 3 | Inversão de matrizes | p. 499 | 03 |
| 4 | Sistemas lineares | p. 508 | 04 |
| 5 | Problemas com sistemas | — | 05 |
| 6 | Espaços vetoriais / combinação linear | p. 15, 39 | 06 |
| 7 | Dependência e independência linear | p. 90 | 07 |
| 8 | Transformações lineares | p. 211 | 08 · **Provinha 8** |
| 9 | Propriedade das transformações lineares | p. 214 | 09 · **Provinha 9** |
| 10 | Valores e vetores próprios | p. 276 | 10 |
| 11 | Determinação de autovalores/autovetores | p. 314 | 11 |
| 12 | Propriedades dos autovalores | p. 316 | 12 |

## Estrutura
- `material/slides/` — slides das aulas
- `material/provas/` — provas e gabaritos
- `material/exercicios/` — listas de exercícios e tarefas
- `projetos/` — trabalhos práticos
- `notas/` — anotações e resumos

## Notas de estudo (resumo por aula + exercícios)
| Arquivo | Conteúdo |
|---------|----------|
| [aula01-matrizes.md](notas/aula01-matrizes.md) | Matrizes: definição, tipos, operações — Tarefa 1 (p. 393) |
| [aula02-determinantes.md](notas/aula02-determinantes.md) | Determinantes (Sarrus, propriedades) — Tarefa 2 (Symbolab) |
| [aula03-inversao-de-matrizes.md](notas/aula03-inversao-de-matrizes.md) | Inversão por operações elementares — Tarefa 3 (p. 499) |
| [aula04-sistemas-de-equacoes-lineares.md](notas/aula04-sistemas-de-equacoes-lineares.md) | Sistemas lineares, forma matricial A·X=B — Tarefa 4 (p. 508) |
| [aula05-problemas-com-sistemas-lineares.md](notas/aula05-problemas-com-sistemas-lineares.md) | Problemas aplicados (UEL, UEPG, ENEM, UNICAMP, UFPE) — Tarefa 5, com 1 exemplo resolvido |
| [aula06-espacos-vetoriais-e-combinacao-linear.md](notas/aula06-espacos-vetoriais-e-combinacao-linear.md) | Espaços vetoriais, combinação linear — Tarefa 6 (p. 15, 39) |
| [aula07-dependencia-e-independencia-linear.md](notas/aula07-dependencia-e-independencia-linear.md) | LI/LD, base e dimensão — Tarefa 7 (p. 90, ex. 47–48 com respostas) |
| [aula08-transformacoes-lineares.md](notas/aula08-transformacoes-lineares.md) | TL, definição + T(0) — Tarefa 8 (p. 211) |
| [revisao-provinha-8-16out-transformacoes-lineares.md](notas/revisao-provinha-8-16out-transformacoes-lineares.md) | **Provinha 8 (16/10):** verificar linearidade + 4.8 do Steinbruch |
| [revisao-provinha-09out-transformacoes-lineares.md](notas/revisao-provinha-09out-transformacoes-lineares.md) | *(antigo)* rascunho TL — redireciona para a Provinha 8 |
| [aula09-propriedade-das-transformacoes-lineares.md](notas/aula09-propriedade-das-transformacoes-lineares.md) | Propriedades das TLs — Tarefa 9 (p. 214) · base da Provinha 9 |
| [revisao-provinha-9-23out-propriedades-tl.md](notas/revisao-provinha-9-23out-propriedades-tl.md) | **Provinha 9 (23/10):** propriedades + T pela base (Steinbruch ~p. 214) |
| [aula10-autovalores-e-autovetores.md](notas/aula10-autovalores-e-autovetores.md) | Autovalores/autovetores (conceito) — Tarefa 10 (p. 276) |
| [aula11-determinacao-de-autovalores-e-autovetores.md](notas/aula11-determinacao-de-autovalores-e-autovetores.md) | Equação característica, passo a passo — Tarefa 11 (p. 314) |
| [aula12-propriedades-dos-autovalores.md](notas/aula12-propriedades-dos-autovalores.md) | Traço, determinante, propriedades — Tarefa 12 (p. 316) |
| [ED1-aplicacoes-matrizes-e-sistemas-em-imagens.md](notas/ED1-aplicacoes-matrizes-e-sistemas-em-imagens.md) | **ED1:** apresentação ~4–5 min (matrizes + sistemas em imagens) |
| [ED1-checklist-apresentacao-18set.md](notas/ED1-checklist-apresentacao-18set.md) | Checklist e timing da apresentação (18/09) |
| [ED1-slides-copiar-colar.md](notas/ED1-slides-copiar-colar.md) | Texto dos 5 slides para colar no PowerPoint |
| [ED1-folha-sistema.md](notas/ED1-folha-sistema.md) | Folha de treino do sistema 3×3 |
| [demo-matrizes-imagens.py](material/exercicios/demo-matrizes-imagens.py) | Demo Python (transposta + contraste) |

## Datas de prova
- **Trab. Nivelamento-1:** 31/Agosto
- **ED1 — Apresentação (Matrizes e Sistemas de Equações):** 04/Set e 11/Set
- **Avaliação 1º Bimestre:** 18/Setembro
- **Trab. Nivelamento-2:** 03/Novembro
- **ED2 — Apresentação (Autovalores e Autovetores):** 06/Nov e 13/Nov
- **Avaliação 2º Bimestre:** 27/Novembro
- **Segunda Chamada:** 04/Dezembro
- **Exame Final:** 11/Dezembro

## Avaliação
- **Estudo Dirigido:** peso 3,0 (média dos trabalhos apresentados)
- **Prova bimestral:** peso 7,0
- Carga horária mínima do Estudo Dirigido: 8h

## Estudo Dirigido
- **ED1:** Aplicações de matrizes e sistemas de equações na área do curso — [notas](notas/ED1-aplicacoes-matrizes-e-sistemas-em-imagens.md)
- **ED2:** Onde a computação usa autovalores (busca, imagens/dados, redes) — [notas](notas/ED2-aplicacoes-autovalores-pagerank.md) · [slides](notas/ED2-slides-copiar-colar.md) · [folha](notas/ED2-folha-calculo.md) · [**app visual**](projetos/ed2-autovalores-app/)

- Referência: STEINBRUCH; WINTERLE. *Álgebra linear*. Pearson, 2014.

## Trabalho de Nivelamento
- **Parte 1** (entrega 31/08): Expressões numéricas/algébricas, porcentagem, proporção e regra de três — vale certificado de 10h
- **Parte 2** (entrega 03/11): Equações de 1º e 2º grau, sistemas — vale certificado de 10h
- Referência: BOULOS, Paulo. *Pré-Cálculo*. Makron Books.

## Metodologia
- Aulas expositivas com participação dos alunos
- PeerInstruction (instrução entre colegas)
- PBL (aprendizagem baseada em problemas)
- Aplicativos: Geogebra, Graphmatica, PhotoMath

## Arquivos no repositório
| Arquivo | Descrição |
|---------|-----------|
| `material/Plano de aula` | Plano de aulas completo |
| `material/Datas de Prova` | Calendário de avaliações (todas as disciplinas) |
| `material/PE AL Ciência` | Programa de ensino (DOCX) |
| `material/slides/AL- Aulas.pdf` | Slides de todas as aulas (referências ao livro) |
| `material/exercicios/Tarefas.pdf` | 12 tarefas ao longo do semestre |
| `material/exercicios/Estudo dirigido.pdf` | Orientação do Estudo Dirigido |
| `material/exercicios/Nivelamento-parte1.pdf` | Nivelamento: expressões, porcentagem, regra de três |
| `material/exercicios/Nivelamento-parte2.pdf` | Nivelamento: equações 1º e 2º grau |
