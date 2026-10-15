# Provinha 8 (16/10) — Transformações lineares (T(0) e definição)

**Disciplina:** Álgebra Linear — Prof.ª Maria Eugênia  
**Quando estudar:** **amanhã 16/10** (provinha sobre o que já foi dado)  
**Conteúdo = Aula 08 / Tarefa 8** — não confundir com a aula do mesmo dia (16/10 ensina Aula 09 → Provinha 9 depois)  
**Aula de referência:** caderno **09/10/2026** + slides aula 08 (pág. 32–36) · livro ~p. 151  
**Fonte dos exercícios 4.8:** Steinbruch, **livro p. 211** = **PDF p. 216**  
**PDF:** `material/Algebra Linear - Steinbruch.pdf`  
**Lista 3:** verificar quais T: ℝ² → ℝ² são lineares  

Ver calendário real: [README — Próximas (2º bim)](../README.md#próximas-2º-bim--plano-vs-real)

---

## Como a professora cobra T(0)

Bate com o caderno da aula **09/10/2026** (scan WhatsApp) e com o slide/livro (~p. 151–152):

1. **Começa pelo vetor nulo.** Em toda linear, T(0) = 0 (“vetor zero é nulo”).
2. **Se T(0) ≠ 0 → T não é linear.** Pode parar.  
   *Caderno Ex1:* T(x,y,z)=(3x+2, 2x−z) → T(0,0,0)=**(2, 0)** ≠ (0,0) → **não é linear**.  
   *(O “z” do caderno parece “3” se ler rápido; no slide a variante é (3x+2, 2y−z) — mesma ideia: constante +2.)*
3. **Se T(0) = 0, ainda não acabou.** Vai para a **condição I**: T(u+v)=T(u)+T(v).  
   *Caderno Ex2/3:* T(x,y)=(x², 3y), T(0,0)=(0,0), mas  
   (x₁+x₂)² = x₁² + 2x₁x₂ + x₂² ≠ x₁² + x₂² → **não verifica a cond. I → não é linear**.
4. Em prova completa, depois da soma ainda vale o escalar T(αu)=αT(u) (ou a forma combinada). Na aula ela já mata o caso com a soma quando aparece x².

**Cuidado com o atalho do caderno:** se estiver escrito algo como “T(0)=0 → é linear”, isso está **incompleto**. O próprio Ex2/3 da mesma página mostra o contrário: T(0)=0 **não basta**. O sentido certo é: *sem* T(0)=0, **não** é linear; *com* T(0)=0, ainda teste a definição.

**Na prova, escreva nessa ordem:** T(0) → se ≠0 pare; se =0, condição I (e II).

---

## Checklist de prova (2 minutos)

- [ ] Calculei **T(0,…,0)** e comparei com o vetor nulo do contradomínio.
- [ ] Se T(0) ≠ 0 → escrevi **“não é linear”** e parei (com a conta).
- [ ] Se T(0) = 0 → **não concluí ainda**; testei soma e escalar com vetores genéricos `(x₁,y₁)`, `(x₂,y₂)` **ou** dei contraexemplo numérico.
- [ ] Desconfiei de: constante somada (`+1`, `+2`), potência (`x²`), produto (`xy`), módulo (`|x|`), seno/cos, raiz.
- [ ] Componentes “só com `ax+by`” (sem produto nem constante) → quase sempre **linear**; mostrei as duas propriedades.

---

## Definição (para copiar na prova)

T: V → W é **linear** se, para todo u, v ∈ V e todo escalar α ∈ ℝ:

1. T(u + v) = T(u) + T(v)
2. T(αu) = α T(u)

**Consequência:** T(0) = 0.  
**Atenção:** T(0) = 0 é necessária, **não suficiente**.

---

# Lista 3 — Verificar quais são lineares  
T: ℝ² → ℝ²

Em todos os itens: primeiro T(0,0); depois definição ou contraexemplo.

---

### a) T(x, y) = (x − 3y, 2x + 5y)

**T(0):**  
T(0,0) = (0 − 0, 0 + 0) = **(0, 0)**. Condição necessária ok.

**Soma.** Sejam u = (x₁, y₁), v = (x₂, y₂).

T(u+v) = T(x₁+x₂, y₁+y₂)  
= ((x₁+x₂) − 3(y₁+y₂), 2(x₁+x₂) + 5(y₁+y₂))  
= (x₁ − 3y₁, 2x₁ + 5y₁) + (x₂ − 3y₂, 2x₂ + 5y₂)  
= T(u) + T(v).

**Escalar.**  
T(αu) = T(αx₁, αy₁) = (αx₁ − 3αy₁, 2αx₁ + 5αy₁) = α(x₁ − 3y₁, 2x₁ + 5y₁) = α T(u).

**Conclusão: LINEAR.**

---

### b) T(x, y) = (y, x)

**T(0):** T(0,0) = (0, 0). Ok.

**Soma.**  
T(u+v) = T(x₁+x₂, y₁+y₂) = (y₁+y₂, x₁+x₂) = (y₁, x₁) + (y₂, x₂) = T(u) + T(v).

**Escalar.**  
T(αu) = T(αx₁, αy₁) = (αy₁, αx₁) = α(y₁, x₁) = α T(u).

**Conclusão: LINEAR.**

---

### c) T(x, y) = (x², y²)

**T(0):** T(0,0) = (0, 0). **Não basta.**

**Contraexemplo (soma).** Tome u = v = (1, 0).

- T(u+v) = T(2, 0) = (4, 0)  
- T(u) + T(v) = (1, 0) + (1, 0) = (2, 0)  

Como 4 ≠ 2, T(u+v) ≠ T(u)+T(v).

**Conclusão: NÃO LINEAR.**

---

### d) T(x, y) = (x + 1, y)

**T(0):** T(0,0) = (0 + 1, 0) = **(1, 0) ≠ (0, 0)**.

**Conclusão: NÃO LINEAR** (já pelo teste do nulo; é uma “translação” na 1ª coordenada).

---

### e) T(x, y) = (y − x, 0)

**T(0):** T(0,0) = (0 − 0, 0) = (0, 0). Ok.

**Soma.**  
T(u+v) = T(x₁+x₂, y₁+y₂) = ((y₁+y₂) − (x₁+x₂), 0)  
= (y₁ − x₁, 0) + (y₂ − x₂, 0) = T(u) + T(v).

**Escalar.**  
T(αu) = T(αx₁, αy₁) = (αy₁ − αx₁, 0) = α(y₁ − x₁, 0) = α T(u).

**Conclusão: LINEAR.**

---

### f) T(x, y) = (|x|, 2y)

**T(0):** T(0,0) = (0, 0). **Não basta.**

**Contraexemplo (escalar / sinal).** Tome u = (1, 0) e α = −1.

- T(αu) = T(−1, 0) = (|−1|, 0) = (1, 0)  
- α T(u) = −1 · T(1, 0) = −(1, 0) = (−1, 0)  

Como (1,0) ≠ (−1,0), T(αu) ≠ α T(u).

(Alternativa pela soma: T(−1,0)+T(1,0)=(1,0)+(1,0)=(2,0), mas T(0,0)=(0,0).)

**Conclusão: NÃO LINEAR.**

---

### g) T(x, y) = (sen x, y)

**T(0):** T(0,0) = (sen 0, 0) = (0, 0). **Não basta.**

**Contraexemplo (soma).** Tome u = v = (π/2, 0).

- T(u+v) = T(π, 0) = (sen π, 0) = (0, 0)  
- T(u) + T(v) = (sen(π/2), 0) + (sen(π/2), 0) = (1, 0) + (1, 0) = (2, 0)  

Como 0 ≠ 2, não é aditiva.

**Conclusão: NÃO LINEAR.**

---

### h) T(x, y) = (xy, x − y)

**T(0):** T(0,0) = (0, 0). **Não basta** (o produto `xy` quebra linearidade).

**Contraexemplo (soma).** Tome u = v = (1, 1).

- T(u+v) = T(2, 2) = (2·2, 2−2) = (4, 0)  
- T(u) + T(v) = (1·1, 1−1) + (1·1, 1−1) = (1, 0) + (1, 0) = (2, 0)  

**Conclusão: NÃO LINEAR.**

---

### i) T(x, y) = (3y, −2x)

**T(0):** T(0,0) = (0, 0). Ok.

**Soma.**  
T(u+v) = T(x₁+x₂, y₁+y₂) = (3(y₁+y₂), −2(x₁+x₂))  
= (3y₁, −2x₁) + (3y₂, −2x₂) = T(u) + T(v).

**Escalar.**  
T(αu) = T(αx₁, αy₁) = (3αy₁, −2αx₁) = α(3y₁, −2x₁) = α T(u).

**Conclusão: LINEAR.**

---

### Resumo rápido da Lista 3

| Item | T(0)=0? | Resultado |
|------|---------|-----------|
| a | sim | **LINEAR** |
| b | sim | **LINEAR** |
| c | sim | **NÃO LINEAR** (x², y²) |
| d | **não** | **NÃO LINEAR** |
| e | sim | **LINEAR** |
| f | sim | **NÃO LINEAR** (\|x\|) |
| g | sim | **NÃO LINEAR** (sen) |
| h | sim | **NÃO LINEAR** (xy) |
| i | sim | **LINEAR** |

**Lineares:** a, b, e, i.  
**Não lineares:** c, d, f, g, h.

---

# 4.8 Problemas propostos (Steinbruch, livro p. 211 / PDF p. 216)

Enunciados confirmados no PDF:

---

### 1) T(x, y) = (3x − 2y, x + 4y); u = (1, 2), v = (3, −1)

Mostrar que T(3u + 4v) = 3T(u) + 4T(v).

**Passo 1 — combinação no domínio**

3u + 4v = 3(1, 2) + 4(3, −1) = (3, 6) + (12, −4) = **(15, 2)**.

**Passo 2 — lado esquerdo**

T(3u + 4v) = T(15, 2)  
= (3·15 − 2·2, 15 + 4·2)  
= (45 − 4, 15 + 8)  
= **(41, 23)**.

**Passo 3 — imagens de u e v**

T(u) = T(1, 2) = (3·1 − 2·2, 1 + 4·2) = (3 − 4, 1 + 8) = **(−1, 9)**  
T(v) = T(3, −1) = (3·3 − 2(−1), 3 + 4(−1)) = (9 + 2, 3 − 4) = **(11, −1)**

**Passo 4 — lado direito**

3T(u) + 4T(v) = 3(−1, 9) + 4(11, −1)  
= (−3, 27) + (44, −4)  
= **(41, 23)**.

Como os dois lados coincidem: **T(3u + 4v) = 3T(u) + 4T(v)** ✓  
(Isso é um caso particular da forma combinada da linearidade; o enunciado já chama T de linear e pede essa verificação numérica.)

---

### 2) T linear com T(u) = 3u e T(v) = u − v

Calcular em função de u e v (usando só a definição de linearidade — **não** precisa da fórmula de T em coordenadas).

#### a) T(u + v)

T(u + v) = T(u) + T(v) = 3u + (u − v) = **4u − v**.

#### b) T(3v)

T(3v) = 3 T(v) = 3(u − v) = **3u − 3v**.

#### c) T(4u − 5v)

T(4u − 5v) = 4 T(u) − 5 T(v)  
= 4(3u) − 5(u − v)  
= 12u − 5u + 5v  
= **7u + 5v**.

---

## Modelo de resposta curta (se o espaço for apertado)

**Não linear por T(0):**  
“T(0,0) = (…) ≠ (0,0). Logo T não é linear.”

**Não linear com T(0)=0:**  
“T(0,0)=(0,0), mas com u=…, v=… temos T(u+v)=… ≠ …=T(u)+T(v). Logo não é linear.”

**Linear:**  
“T(0,0)=(0,0). Sejam u=(x₁,y₁), v=(x₂,y₂). [mostra soma]. [mostra escalar]. Logo T é linear.”

---

## O que decorar amanhã (mínimo)

1. Definição em 2 linhas + atalho T(αu+βv).  
2. Teste rápido T(0).  
3. “T(0)=0 não basta” — um exemplo mental: x² ou xy ou |x| ou sen x.  
4. Contas do tipo 4.8 item 1 (substituir combinação e comparar lados) e item 2 (distribuir T sem fórmula).
