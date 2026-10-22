# Provinha 9 (23/10) — Propriedades das transformações lineares

**Disciplina:** Álgebra Linear — Prof.ª Maria Eugênia  
**Quando estudar:** **amanhã 23/10** (estimado)  
**Conteúdo = Aula 09 / Tarefa 9** — propriedades da TL (combinação linear; T definida pela base)  
**Não é a Provinha 8:** P8 cobriu *verificar se é linear* + T(0). Aqui o foco é **usar** a linearidade.  
**Aula de referência:** [aula09](aula09-propriedade-das-transformacoes-lineares.md) · slides pág. 37–39 · livro ~p. 160 (teoria) / **p. 214** (Tarefa 9)  
**PDF:** `material/Algebra Linear - Steinbruch.pdf`  
**Pré-requisito curto (P8):** T linear ⇒ T(0)=0; definição T(u+v)=T(u)+T(v) e T(αu)=αT(u).

---

## O que a professora cobra (mapa mental)

Se T: V → W é **linear**, então:

1. **T(0) = 0** (já visto na P8 — necessário).
2. **T(−v) = −T(v)** e **T(u − v) = T(u) − T(v)**.
3. **Preserva combinação linear:**  
   T(α₁v₁ + … + αₖvₖ) = α₁T(v₁) + … + αₖT(vₖ).
4. **Determinada pela base:** se B = {v₁,…,vₙ} é base de V e você conhece T(v₁),…,T(vₙ), então conhece T(v) para **todo** v ∈ V (escreva v na base e “passe o T”).
5. (Se cair) **Injetora** ⇔ N(T) = {0}; **sobrejetora** (com dim V = dim W) ⇔ Im(T) = W.

**Na prova, o padrão mais provável:** “dados T nos vetores de uma base, achar T(x,y) / T(x,y,z)” ou “achar v com T(v) = w”.

---

## Checklist de prova (2 minutos)

- [ ] Li o enunciado: T **já é** linear? Então **não** preciso retestar a definição — só usar as propriedades.
- [ ] Se pediu T(x,…) a partir de valores na base: (1) confirmei que o conjunto é base / LI; (2) escrevi o vetor genérico como combinação; (3) apliquei T termo a termo.
- [ ] Contas: sistema para os coeficientes αᵢ → substituí nas imagens T(vᵢ).
- [ ] Se pediu pré-imagem T(v)=w: montei o sistema com a fórmula de T e resolvi.
- [ ] Se pediu N(T) / Im(T) / injetora: T(v)=0 ou geradores das colunas/imagens dos vetores da base.
- [ ] Não confundi: **achar a fórmula de T** ≠ **verificar se uma fórmula é linear** (isso foi P8).

---

## Pré-requisito em 30 segundos (P8)

T linear ⇒ T(0)=0.  
T(0)=0 **não basta** para ser linear (ex.: T(x,y)=(x²,y)).  
Na P9, se o enunciado **já diz** “seja T linear…”, use a propriedade da combinação e siga.

---

## Propriedades para copiar na prova

### Forma combinada

T(αu + βv) = α T(u) + β T(v).

### T definida pela base

Se {v₁,…,vₙ} é base de V e v = α₁v₁ + … + αₙvₙ, então

T(v) = α₁ T(v₁) + … + αₙ T(vₙ).

### Opostos e diferença (prova de 1 linha)

T(−v) = T((−1)v) = (−1)T(v) = −T(v).  
T(u − v) = T(u + (−v)) = T(u) − T(v).

---

# Exemplos resolvidos (estilo prova)

## Exemplo A — Teoria p. 160–162: T a partir da base

T: ℝ³ → ℝ² linear, B = {v₁, v₂, v₃} base de ℝ³ com  
v₁ = (0,1,0), v₂ = (1,0,1), v₃ = (1,1,0),  
T(v₁)=(1,−2), T(v₂)=(3,1), T(v₃)=(0,2).  
Achar T(5, 3, −2).

**Passo 1 — combinar o vetor na base**

(5, 3, −2) = α₁(0,1,0) + α₂(1,0,1) + α₃(1,1,0)

Sistema:  
α₂ + α₃ = 5  
α₁ + α₃ = 3  
α₂ = −2  

→ α₂ = −2, α₃ = 7, α₁ = −4.

**Passo 2 — aplicar T**

T(5,3,−2) = −4 T(v₁) − 2 T(v₂) + 7 T(v₃)  
= −4(1,−2) − 2(3,1) + 7(0,2)  
= (−4, 8) + (−6, −2) + (0, 14)  
= **(−10, 20)**.

---

## Exemplo B — Steinbruch 4.8 item 7 (livro p. 214) ★

a) Determinar a TL T: ℝ² → ℝ³ tal que  
T(−1, 1) = (3, 2, 1) e T(0, 1) = (1, 1, 0).

**Passo 1 — base.** {(−1,1), (0,1)} é LI (não são múltiplos) e tem 2 vetores em ℝ² → base.

**Passo 2 — combinar (x,y)**

(x, y) = a(−1, 1) + b(0, 1)  
⇒ −a = x, a + b = y  
⇒ a = −x, b = x + y.

**Passo 3 — fórmula**

T(x, y) = a T(−1,1) + b T(0,1)  
= (−x)(3,2,1) + (x+y)(1,1,0)  
= (−3x, −2x, −x) + (x+y, x+y, 0)  
= **(−2x + y, −x + y, −x)**.

b) Encontrar v ∈ ℝ² com T(v) = (−2, 1, −3).

(−2x + y, −x + y, −x) = (−2, 1, −3)  
3ª coord.: −x = −3 ⇒ **x = 3**  
1ª: −6 + y = −2 ⇒ **y = 4**  
2ª (checagem): −3 + 4 = 1 ✓  

**v = (3, 4)**.

---

## Exemplo C — Steinbruch 4.8 item 9 (p. 214)

T: ℝ³ → ℝ² linear com  
T(1,1,1)=(1,2), T(1,1,0)=(2,3), T(1,0,0)=(3,4).

a) Achar T(x, y, z).

(x,y,z) = a(1,1,1) + b(1,1,0) + c(1,0,0)  
⇒ a = z, b = y − z, c = x − y.

T(x,y,z) = z(1,2) + (y−z)(2,3) + (x−y)(3,4)  
= (z + 2y − 2z + 3x − 3y , 2z + 3y − 3z + 4x − 4y)  
= **(3x − y − z, 4x − y − z)**.

b) T(v)=(−3,−2):  
3x − y − z = −3  
4x − y − z = −2  
⇒ x = 1 e y + z = 6 (infinitas soluções).  
Uma resposta válida: **v = (1, 6, 0)** (z=0).

c) T(v)=(0,0): x=0 e y=−z ⇒ **v = t(0, −1, 1)**, t ∈ ℝ.  
(Em particular N(T) ≠ {0} ⇒ T **não** é injetora.)

---

## Exemplo D — Distribuir T sem fórmula (eco da P8, item 2)

T linear, T(u)=3u, T(v)=u−v.

T(4u − 5v) = 4T(u) − 5T(v) = 4(3u) − 5(u−v) = **7u + 5v**.

Não precisa de coordenadas: só a propriedade 3.

---

## Exemplo E — Núcleo rápido (4.8 item 12)

T(x,y)=(2x+y, 4x+2y).  
T(v)=0 ⇔ 2x+y=0 (a 2ª equação é o dobro) ⇔ y=−2x.

| vetor | em N(T)? |
|-------|----------|
| (1, −2) | **sim** |
| (2, −3) | não (2·2−3=1≠0) |
| (−3, 6) | **sim** |

---

## Armadilhas clássicas

1. **Tratar como P8:** ficar verificando linearidade quando o enunciado já diz que T é linear — perde tempo.
2. **Esquecer o sistema da base:** chutar T(x,y)=x T(v₁)+y T(v₂) só funciona se {v₁,v₂} for a **base canônica**. Fora dela, ache α, β primeiro.
3. **Base inválida:** se os vetores dados forem LD, a T pode não ficar bem definida / o sistema fica inconsistente — confira LI.
4. **Confundir domínio e contradomínio:** T: ℝ²→ℝ³ tem imagem em ℝ³; N(T) ⊂ ℝ².
5. **Uma pré-imagem ≠ única:** se N(T)≠{0}, T(v)=w pode ter infinitas soluções (Ex. C-b).
6. **Sinal do oposto:** T(−v)=−T(v), não “T(v) com sinal trocado no domínio sem justificar”.

---

## Modelo de resposta curta

**T pela base:**  
“{(v₁,…)} é base. (x,…) = α₁v₁+…. Sistema → αᵢ=….  
T(x,…) = α₁T(v₁)+… = (fórmula).”

**Pré-imagem:**  
“T(x,…)=w ⇒ sistema … ⇒ v=(…).”

**Injetora:**  
“N(T)={0} ⇔ só a solução nula de T(v)=0 ⇔ injetora.”

---

## O que estudar em 30 min (ordem)

1. **5 min** — releia as 4 propriedades do mapa mental + prova de T(−v).  
2. **10 min** — refaça o **Exemplo B** (item 7) sem olhar a conta.  
3. **10 min** — refaça o **Exemplo C-a** (achar T(x,y,z)).  
4. **5 min** — checklist + uma pergunta de N(T) (Exemplo E).

**Mínimo para decorar:** “escrever na base → aplicar T nos coeficientes”; T(−v)=−T(v); injetora ⇔ N(T)={0}.

---

## Fontes

- [Aula 09](aula09-propriedade-das-transformacoes-lineares.md)  
- Steinbruch §4.1.2 (teoria ~p. 160) · 4.8 itens a partir da **p. 214** (Tarefa 9)  
- Contraste P8: [revisao-provinha-8-16out-transformacoes-lineares.md](revisao-provinha-8-16out-transformacoes-lineares.md)
