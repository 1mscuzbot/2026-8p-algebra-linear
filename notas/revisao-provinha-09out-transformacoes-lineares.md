# Provinha 09/10 — Transformações lineares

**O que você faltou:** no plano, 02/10 era dependência linear (aula 07) e 09/10 era transformações lineares (aula 08). A aula 07 foi adiantada. No dia **02/10** a professora deu a **aula 08**. A provinha de **09/10** é sobre isso.

**Slide:** `material/slides/202485_17036_AL- Aulas.pdf`, páginas 32–36 (livro Steinbruch, p. 151).  
O que está no slide: definição, a propriedade T(0) = 0, identidade, transformação nula, e “verificar quais são lineares”. Núcleo e imagem estão no nome do plano do dia, mas **não aparecem nessas páginas**. Estuda primeiro o que está no slide. O núcleo fica no final, como extra.

---

## 1. O que é

T: V → W é **transformação linear** quando, para todo u, v em V e todo escalar α:

1. **T(u + v) = T(u) + T(v)**
2. **T(αu) = α T(u)**

Se V = W, chama-se **operador linear**.

Atalho equivalente (quando pedir “mostre de uma vez”): T(αu + βv) = α T(u) + β T(v).

**Exemplo do slide.** T: ℝ² → ℝ³, T(x, y) = (3x, −2y, x − y).

T(2, 1) = (3·2, −2·1, 2 − 1) = **(6, −2, 1)**.

---

## 2. Como provar que é linear (modelo do slide)

T: ℝ² → ℝ³, T(x, y) = (3x, −2y, x − y).

Sejam u = (x₁, y₁) e v = (x₂, y₂).

**Soma**

T(u + v) = T(x₁+x₂, y₁+y₂) = (3(x₁+x₂), −2(y₁+y₂), (x₁+x₂) − (y₁+y₂))

= (3x₁, −2y₁, x₁−y₁) + (3x₂, −2y₂, x₂−y₂) = T(u) + T(v).

**Escalar**

T(αu) = T(αx₁, αy₁) = (3αx₁, −2αy₁, αx₁ − αy₁) = α (3x₁, −2y₁, x₁−y₁) = α T(u).

Logo T é linear.

---

## 3. Atalho da prova: T(0) tem que ser 0

Se T é linear, **T(0) = 0**.

Se T(0) ≠ 0, **já não é linear**. Não precisa testar soma e escalar.

**Exemplo do slide (não é linear).** T: ℝ³ → ℝ², T(x, y, z) = (3x + 2, 2y − z).

T(0, 0, 0) = (2, 0) ≠ (0, 0).

**Cuidado (também está no slide).** T(0) = 0 **não garante** que seja linear.  
T: ℝ² → ℝ², T(x, y) = (x², 2y) manda zero em zero, mas

T(u+v) = ((x₁+x₂)², 2(y₁+y₂)) = (x₁² + 2x₁x₂ + x₂², …)

T(u)+T(v) = (x₁² + x₂², …)

O termo 2x₁x₂ sobra. Não é linear.

**Tradução no plano** também não é linear: T(x, y) = (x + 2, y + 3), porque T(0, 0) = (2, 3) ≠ (0, 0).

---

## 4. Dois casos que sempre são lineares

| Nome | Regra | Por quê |
|------|--------|---------|
| **Identidade** I: V → V | I(v) = v | I(u+v) = u+v = I(u)+I(v) e I(αu) = αu = α I(u) |
| **Nula** T: V → W | T(v) = 0 | T(u+v) = 0 = 0+0 e T(αu) = 0 = α·0 |

---

## 5. Roteiro na provinha

1. Calcule **T(0)**. Se não der 0, escreva “não é linear” e pare.
2. Se der 0, prove as **duas** propriedades com vetores genéricos (x₁, y₁) e (x₂, y₂).
3. Desconfie de **quadrado**, produto xy, raiz, ou **constante somada** (o “+2”, “+3”).
4. Some componente a componente. Não misture a conta das duas propriedades no mesmo parágrafo.

---

## 6. Exercícios (faz no papel)

**1.** T: ℝ² → ℝ², T(x, y) = (2x − y, x + 3y). É linear? Prove ou dê o contraexemplo.

**2.** T: ℝ² → ℝ³, T(x, y) = (x + 1, y, x − y). É linear?

**3.** T: ℝ³ → ℝ², T(x, y, z) = (x + y + z, 2x). É linear? Prove.

**4.** T: ℝ² → ℝ², T(x, y) = (xy, x). T(0, 0) = (0, 0). Isso basta para ser linear?

**5.** T: ℝ² → ℝ², T(x, y) = (0, 0). Que transformação é essa? É linear?

**6. (extra — só se ela pedir núcleo)** T: ℝ² → ℝ², T(x, y) = (x + y, x + y). Ache N(T) = {v | T(v) = 0} e diga uma base.

---

## Gabarito

**1. Linear.** u = (x₁, y₁), v = (x₂, y₂).

T(u+v) = (2(x₁+x₂) − (y₁+y₂), (x₁+x₂) + 3(y₁+y₂)) = (2x₁−y₁, x₁+3y₁) + (2x₂−y₂, x₂+3y₂) = T(u)+T(v).

T(αu) = (2αx₁ − αy₁, αx₁ + 3αy₁) = α T(u).

**2. Não.** T(0, 0) = (1, 0, 0) ≠ (0, 0, 0).

**3. Linear.** u = (x₁, y₁, z₁), v = (x₂, y₂, z₂).

T(u+v) = ((x₁+x₂)+(y₁+y₂)+(z₁+z₂), 2(x₁+x₂)) = (x₁+y₁+z₁, 2x₁) + (x₂+y₂+z₂, 2x₂) = T(u)+T(v).

T(αu) = (αx₁+αy₁+αz₁, 2αx₁) = α T(u).

**4. Não basta.** T(0, 0) = (0, 0), mas a soma falha. Com u = v = (1, 1):

T(u+v) = T(2, 2) = (2·2, 2) = (4, 2)

T(u)+T(v) = (1, 1) + (1, 1) = (2, 2)

(4, 2) ≠ (2, 2). Não é linear.

**5.** Transformação **nula**. É linear (seção 4 do resumo).

**6.** T(x, y) = (0, 0) ⇒ x + y = 0 ⇒ y = −x. N(T) = {(x, −x) | x ∈ ℝ} = span{(1, −1)}. Base: {(1, −1)}.
