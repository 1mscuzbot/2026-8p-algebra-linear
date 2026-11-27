# Refazer provinhas — Álgebra Linear (01/10 e 16/10)

**Disciplina:** Álgebra Linear — Prof.ª Maria Eugênia  
**Livro:** Steinbruch; Winterle — *Álgebra linear*  
**Aviso:** não há enunciados oficiais dessas datas no tip do repo. Tudo abaixo é **simulado no estilo da professora** (Tarefa + caderno + padrão das outras provinhas).  
**Cópia no Project store:** `docs/algebra-refazer-provinhas-01out-e-16out.md`

---

## 1) O que cada data cobra

### 01/10 — LI / LD, base e dimensão *(Provinha 7, inferida)*

| | |
|---|---|
| **Conteúdo** | Dependência e independência linear; base; dimensão |
| **Aula / tarefa** | [Aula 07](aula07-dependencia-e-independencia-linear.md) · **Tarefa 7** (Steinbruch **p. 90**, ex. 47–48) |
| **Slides** | `material/slides/202485_17036_AL- Aulas.pdf` (págs. 30–31) |
| **Aula anterior (contexto)** | [Aula 06](aula06-espacos-vetoriais-e-combinacao-linear.md) — espaços / combinação linear (25/09) |
| **Arquivo nomeado “01/10”** | **Não existe** no repo |

**Ambiguidade 01 vs 02/10 (1 parágrafo).** No plano oficial, **02/10** é a data da **Aula 07** (LI/LD, base, dimensão); **01/10** não aparece em nenhuma nota ou revisão nomeada. O padrão real das provinhas é “aula numa sexta → cobrada na sexta seguinte”, então a cobrada no início de outubro pode ter sido (a) o conteúdo da Aula 06 (25/09) ou (b) já o núcleo da Aula 07. Como o pedido foi refazer **01/10** e o material mais próximo no calendário/tarefa é LI/LD + base + dimensão (Tarefa 7), este roteiro trata a data assim — e, se a professora cobrou combinação linear “pura” da Aula 06, o mesmo método (sistema / escalonamento) resolve.

### 16/10 — Provinha 8 (confirmada)

| | |
|---|---|
| **Conteúdo** | Transformações lineares: definição, **T(0)**, verificar linearidade |
| **Aula / tarefa** | Aula 08 · **Tarefa 8** · Steinbruch **4.8** (livro p. 211 / PDF p. 216) |
| **Revisão canônica** | [revisao-provinha-8-16out-transformacoes-lineares.md](revisao-provinha-8-16out-transformacoes-lineares.md) |
| **Lista 3** | Verificar quais \(T:\mathbb{R}^2\to\mathbb{R}^2\) são lineares (**itens a–i** — **não duplicar aqui**: repetir a–i na revisão acima) |
| **No mesmo dia (aula nova)** | Aula 09 (propriedades) → base da Provinha 9; **não** é o foco do refazer de 16/10 |

**Ordem que a professora cobra:** \(T(0)\) primeiro → se \(\neq 0\), pare (“não linear”); se \(=0\), ainda teste soma e escalar. \(T(0)=0\) **não basta**.

---

## 2) Simulados (estilo professora) + gabarito passo a passo

### Simulado A — estilo 01/10 (LI/LD + base + dimensão)

> **Simulado** — não é enunciado oficial. Justifique com conta (como na Tarefa 7).

#### Q1. Classifique LI ou LD e justifique

\[
S = \{(1,0,1),\ (0,1,1),\ (1,1,2)\} \subset \mathbb{R}^3
\]

**Gabarito.** Montar a combinação nula \(a(1,0,1)+b(0,1,1)+c(1,1,2)=(0,0,0)\):

\[
\begin{cases}
a + c = 0 \\
b + c = 0 \\
a + b + 2c = 0
\end{cases}
\]

Das duas primeiras: \(a=-c\), \(b=-c\). Na terceira: \(-c-c+2c=0\) (sempre verdade). Há solução não trivial (ex.: \(c=1\Rightarrow a=b=-1\)).  
**Conclusão: LD** (o 3º vetor é soma dos dois primeiros).

#### Q2. Dois vetores — atalho da professora

\[
A=\{(2,−4),\ (−1,2)\} \subset \mathbb{R}^2
\]

**Gabarito.** Com só dois vetores: LD ⇔ um é múltiplo do outro.  
\((-1,2)=-\frac12(2,-4)\). **LD.**

#### Q3. Um vetor só / vetor nulo

(a) \(\{(0,0,0)\}\) (b) \(\{(3,−1,2)\}\)

**Gabarito.**  
(a) Conjunto só com o nulo → **LD**.  
(b) Um único vetor não nulo → **LI**.

#### Q4. Base e dimensão

Mostre que \(B=\{(1,1),\ (1,-1)\}\) é base de \(\mathbb{R}^2\) e diga \(\dim\mathbb{R}^2\).

**Gabarito.**  
1. **LI:** \(a(1,1)+b(1,-1)=(0,0)\Rightarrow a+b=0,\ a-b=0\Rightarrow a=b=0\).  
2. **Gera \(\mathbb{R}^2\):** 2 vetores LI em espaço de dim 2 (ou: para \((x,y)\), resolver \(a+b=x,\ a-b=y\) → \(a=\frac{x+y}{2},\ b=\frac{x-y}{2}\)).  
3. Logo \(B\) é **base** e \(\dim\mathbb{R}^2=2\) (número de vetores da base). Base canônica também tem 2 vetores.

#### Q5 *(estilo Tarefa 7 / P₂)*. Em \(P_2\) (polinômios grau ≤ 2)

\[
\{1+x,\ x+x^2,\ 1+x^2\}
\]

LI ou LD?

**Gabarito.** \(a(1+x)+b(x+x^2)+c(1+x^2)=0\)  
\(\Rightarrow (a+c) + (a+b)x + (b+c)x^2 = 0\)  
\(\Rightarrow a+c=0,\ a+b=0,\ b+c=0\). De \(a=-c\), \(b=-c\): 3ª eq. \(-c-c=0\Rightarrow c=0\Rightarrow a=b=0\).  
**LI.** (Respostas-guia da Tarefa 7 no livro: 47 a–g e 48 a–d — treinar justificando, não só memorizar.)

---

### Simulado B — estilo 16/10 (Provinha 8 / TL)

> **Simulado** — não é enunciado oficial. Espelha caderno 09/10 + Lista 3 + 4.8.

#### Q1. Teste do nulo (caderno)

\[
T(x,y,z)=(3x+2,\ 2x-z)
\]

**Gabarito.** \(T(0,0,0)=(2,0)\neq(0,0)\).  
**Não é linear** (pode parar).

#### Q2. \(T(0)=0\) não basta

\[
T(x,y)=(x^2,\ 3y)
\]

**Gabarito.** \(T(0,0)=(0,0)\), mas com \(u=v=(1,0)\):  
\(T(u+v)=T(2,0)=(4,0)\), \(T(u)+T(v)=(1,0)+(1,0)=(2,0)\).  
\(4\neq 2\) → **não linear**.

#### Q3. Linear “bonita” (só \(ax+by\))

\[
T(x,y)=(2x-y,\ x+4y)
\]

**Gabarito.** \(T(0,0)=(0,0)\).  
Soma: \(T(u+v)=(2(x_1+x_2)-(y_1+y_2),\ \ldots)=T(u)+T(v)\).  
Escalar: \(T(\alpha u)=\alpha T(u)\).  
**Linear.**

#### Q4. Estilo Steinbruch 4.8 — combinação

\(T(x,y)=(3x-2y,\ x+4y)\), \(u=(1,2)\), \(v=(3,-1)\).  
Mostre \(T(3u+4v)=3T(u)+4T(v)\).

**Gabarito (resumo).** \(3u+4v=(15,2)\); \(T(15,2)=(41,23)\).  
\(T(u)=(-1,9)\), \(T(v)=(11,-1)\); \(3T(u)+4T(v)=(41,23)\). Contas completas em [revisao-provinha-8-16out-transformacoes-lineares.md](revisao-provinha-8-16out-transformacoes-lineares.md) (item 4.8–1).

#### Q5. Distribuir T sem fórmula (4.8–2)

T linear, \(T(u)=3u\), \(T(v)=u-v\). Calcule \(T(4u-5v)\).

**Gabarito.** \(T(4u-5v)=4T(u)-5T(v)=4(3u)-5(u-v)=12u-5u+5v=\mathbf{7u+5v}\).

#### Lista 3 (a–i) — não duplicar

**Repetir exercícios a–i** em [revisao-provinha-8-16out-transformacoes-lineares.md](revisao-provinha-8-16out-transformacoes-lineares.md) (seção Lista 3).

**Resumo:** lineares **a, b, e, i** · não lineares **c, d, f, g, h**.

---

## 3) Checklist de 2 min (antes de entregar)

### Se for a de 01/10 (LI/LD)

- [ ] Escrevi a combinação nula \(a_1v_1+\cdots+a_kv_k=0\) (ou “múltiplo” se forem só 2).
- [ ] Concluí **LI** só se a única solução for todos \(a_i=0\); senão **LD**.
- [ ] Nulo sozinho → LD; um não nulo → LI; parte LD ⇒ o todo LD.
- [ ] Base = LI **e** gera; dimensão = nº de vetores da base.
- [ ] Justifiquei com conta (Tarefa 7 pede “por quê”).

### Se for a de 16/10 (TL)

- [ ] Calculei **T(0,…,0)** e comparei com o nulo do contradomínio.
- [ ] Se \(T(0)\neq 0\) → “não linear” + parei.
- [ ] Se \(T(0)=0\) → **não concluí ainda**; testei soma/escalar ou dei contraexemplo.
- [ ] Desconfiei de: constante (`+1`), \(x^2\), \(xy\), \(|x|\), sen/cos, raiz.
- [ ] Componentes só \(ax+by\) → mostrei as duas propriedades.

---

## 4) Como estudar em ~40 min

| Tempo | 01/10 | 16/10 |
|------|--------|--------|
| 0–10 | Reler Aula 07 (definições + atalhos) | Reler bloco T(0) na revisão P8 |
| 10–30 | Fazer Simulado A Q1–Q5 + 2 itens da Tarefa 7 (p. 90) | Simulado B Q1–Q5 + **repetir Lista 3 a–i** |
| 30–40 | Checklist LI/LD | Checklist T(0) + 1 item 4.8 |

---

## Fontes checadas

| Fonte | Path |
|-------|------|
| README (mapa + P8 16/10) | [README.md](../README.md) |
| Aula 07 | [aula07-dependencia-e-independencia-linear.md](aula07-dependencia-e-independencia-linear.md) |
| Aula 06 | [aula06-espacos-vetoriais-e-combinacao-linear.md](aula06-espacos-vetoriais-e-combinacao-linear.md) |
| Revisão P8 | [revisao-provinha-8-16out-transformacoes-lineares.md](revisao-provinha-8-16out-transformacoes-lineares.md) |
| Plano / Tarefas | `material/…Plano…pdf`, `material/exercicios/…Tarefas.pdf`, Steinbruch PDF |
