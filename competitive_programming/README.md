Of course. Here is a purely paper-based math roadmap for Competitive Programming, structured like a mathematician's personal notebook. It focuses on the core identities, formulas, and manual reasoning patterns you need to solve problems before a single line of code is written.

***

# 🧠 Competitive Programming Math Roadmap
*A Paper-Based Approach*

---

## **I. Foundations: Arithmetic & Logic**

**1. Summation Formulas**
- \( 1 + 2 + \dots + n = \frac{n(n+1)}{2} \)
- \( 1^2 + 2^2 + \dots + n^2 = \frac{n(n+1)(2n+1)}{6} \)
- \( 1^3 + 2^3 + \dots + n^3 = \left[\frac{n(n+1)}{2}\right]^2 \)
- *Pattern:* Sum of first `n` odd numbers = \( n^2 \). Sum of first `n` even numbers = \( n(n+1) \).

**2. Divisibility & GCD/LCM**
- **Euclid's GCD Algorithm (by hand):**
  \( \text{gcd}(a, b) = \text{gcd}(b, a \bmod b) \). Repeat until remainder is 0.
- **LCM from GCD:**
  \( \text{lcm}(a, b) = \frac{a \times b}{\text{gcd}(a, b)} \)
- **Prime Factorization Method:**
  For \( a = p_1^{a_1}p_2^{a_2}... \), \( b = p_1^{b_1}p_2^{b_2}... \)
  - \( \text{gcd}(a, b) = p_1^{\min(a_1, b_1)}p_2^{\min(a_2, b_2)}\dots \)
  - \( \text{lcm}(a, b) = p_1^{\max(a_1, b_1)}p_2^{\max(a_2, b_2)}\dots \)

---

## **II. Number Theory Core**

**1. Modular Arithmetic**
- \( (a + b) \bmod m = ((a \bmod m) + (b \bmod m)) \bmod m \)
- \( (a - b) \bmod m = ((a \bmod m) - (b \bmod m) + m) \bmod m \) *(+m ensures non-negative)*
- \( (a \times b) \bmod m = ((a \bmod m) \times (b \bmod m)) \bmod m \)
- **Fermat's Little Theorem (Prime Modulus):**
  If \( p \) is prime and \( \text{gcd}(a, p) = 1 \), then \( a^{p-1} \equiv 1 \pmod{p} \).
  - **Corollary (Modular Inverse):** \( a^{-1} \equiv a^{p-2} \pmod{p} \)

**2. Prime Numbers**
- **Trial Division:** Test divisibility by primes \( \leq \lfloor \sqrt{n} \rfloor \).
- **Sieve of Eratosthenes (Conceptual):** List numbers 2..n. Mark multiples of each prime starting from 2. Unmarked numbers are prime.
- **Prime Factorization:** Repeatedly divide by smallest prime factor.

**Example (n=84):**
\( 84 \div 2 = 42 \)
\( 42 \div 2 = 21 \)
\( 21 \div 3 = 7 \)
∴ \( 84 = 2^2 \times 3 \times 7 \)

---

## **III. Combinatorics & Probability**

**1. Counting Principles**
- **Factorial:** \( n! = 1 \times 2 \times \dots \times n \)
- **Permutations:** \( nPr = \frac{n!}{(n-r)!} \) (arrangements of `r` from `n`)
- **Combinations:** \( nCr = \binom{n}{r} = \frac{n!}{r!(n-r)!} \) (selections of `r` from `n`)
- **Pascal's Identity:** \( \binom{n}{r} = \binom{n-1}{r-1} + \binom{n-1}{r} \)

**2. Probability Basics**
- \( P(E) = \frac{\text{Favorable Outcomes}}{\text{Total Outcomes}} \)
- **Expected Value (Discrete):** \( E[X] = \sum x_i \cdot P(x_i) \)

---

## **IV. Sequences & Series**

| Type | Formula for Sum \( S_n \) |
| :--- | :--- |
| Arithmetic <br> (First term \( a \), difference \( d \)) | \( S_n = \frac{n}{2}[2a + (n-1)d] \) |
| Geometric <br> (First term \( a \), ratio \( r \neq 1 \)) | \( S_n = a \cdot \frac{r^n - 1}{r - 1} \) |
| Infinite Geometric <br> (\( \lvert r \rvert < 1 \)) | \( S_{\infty} = \frac{a}{1 - r} \) |

---

## **V. Algebra & Functions**

**1. Exponentiation & Logarithms**
- \( a^{m+n} = a^m \cdot a^n \)
- \( (a^m)^n = a^{m \cdot n} \)
- \( \log(ab) = \log a + \log b \)
- \( \log(a^b) = b \cdot \log a \)
- \( \log_a b = \frac{\log_c b}{\log_c a} \) (Change of Base)

**2. Function Growth Rate (for Complexity)**
\( 1 < \log n < n < n \log n < n^2 < n^3 < 2^n < n! \)
*Use L'Hôpital's rule or compare ratios \( \frac{f(n+1)}{f(n)} \) to prove.*

---

## **VI. Geometry & Coordinate Systems**

**1. Key Formulas**
- **Distance:** \( d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2} \)
- **Midpoint:** \( M = \left( \frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2} \right) \)
- **Slope:** \( m = \frac{y_2 - y_1}{x_2 - x_1} \)
- **Area of Triangle (Vertices A, B, C):**
  \( \text{Area} = \frac{1}{2} | x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2) | \)
- **Circle:** \( (x - h)^2 + (y - k)^2 = r^2 \)

**2. Shoelace Theorem (Polygon Area)**
For polygon with vertices \( (x_1, y_1), (x_2, y_2), \dots, (x_n, y_n) \):
\[
\text{Area} = \frac{1}{2} \left| \sum_{i=1}^{n-1} (x_i y_{i+1} - x_{i+1} y_i) + (x_n y_1 - x_1 y_n) \right|
\]
*Calculate by creating a table and summing diagonals.*

---

## **VII. Advanced Concepts**

**1. Euler's Totient Function \( \phi(n) \)**
- For \( n = p_1^{k_1}p_2^{k_2}\dots \), \( \phi(n) = n \left(1 - \frac{1}{p_1}\right)\left(1 - \frac{1}{p_2}\right)\dots \)
- Counts integers ≤ n that are coprime to n.

**2. Inclusion-Exclusion Principle**
For two sets: \( |A \cup B| = |A| + |B| - |A \cap B| \)
For three sets: \( |A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C| \)
*Pattern: Add singles, subtract pairs, add triple, etc.*

**3. Catalan Numbers**
\( C_n = \frac{1}{n+1}\binom{2n}{n} \)
*Applications: Valid parenthesis expressions, binary tree counts.*

**4. Chinese Remainder Theorem (CRT)**
Given:
\( x \equiv a_1 \pmod{m_1} \)
\( x \equiv a_2 \pmod{m_2} \)
...
If \( m_1, m_2, \dots \) are coprime, a unique solution modulo \( M = m_1 m_2 \dots \) exists.
*Manual Solve:* Find \( M \), then \( M_i = M/m_i \), then find \( y_i \) such that \( M_i y_i \equiv 1 \pmod{m_i} \). Solution: \( x = \sum a_i M_i y_i \mod M \).

---

## **VIII. Special Tricks & Shortcuts**

- **Trailing Zeros in n!:** \( Z = \left\lfloor \frac{n}{5} \right\rfloor + \left\lfloor \frac{n}{25} \right\rfloor + \left\lfloor \frac{n}{125} \right\rfloor + \dots \)
- **Digit Sum:** Sum of digits of a number. Repeated sum converges to its digital root (\( n \bmod 9 \), with 0 becoming 9).
- **Binary Exponentiation (Concept):** To compute \( a^b \), write `b` in binary. Square the base and multiply into the result when the bit is set.
  *Example: \( a^{13} = a^{1101_2} = a^8 \cdot a^4 \cdot a^1 \)*

***

Perfect. Here is the **Advanced Competitive Programming Math Roadmap (Part 2)** in the same paper-style notebook format.

---

# 🧠 **Advanced CP Math Roadmap II**
*Paper Notes for Intermediate/Expert Level*

---

## **XIII. Extended Euclidean Algorithm**

**🔹 Problem:** Solve \( ax + by = \gcd(a, b) \) for integers \( x, y \).

**🔹 Process (Paper Method):**
1. Perform Euclidean algorithm, keeping track of remainders
2. **Back-substitute** to express gcd in terms of original a, b

**Example:** Solve \( 81x + 57y = \gcd(81, 57) \)

**Step 1 - Forward pass:**
\[
\begin{align*}
81 &= 1 \cdot 57 + 24 \\
57 &= 2 \cdot 24 + 9 \\
24 &= 2 \cdot 9 + 6 \\
9 &= 1 \cdot 6 + 3 \\
6 &= 2 \cdot 3 + 0 \quad \therefore \gcd = 3
\end{align*}
\]

**Step 2 - Back substitution:**
\[
\begin{align*}
3 &= 9 - 1 \cdot 6 \\
  &= 9 - 1 \cdot (24 - 2 \cdot 9) = 3 \cdot 9 - 1 \cdot 24 \\
  &= 3 \cdot (57 - 2 \cdot 24) - 1 \cdot 24 = 3 \cdot 57 - 7 \cdot 24 \\
  &= 3 \cdot 57 - 7 \cdot (81 - 1 \cdot 57) = 10 \cdot 57 - 7 \cdot 81
\end{align*}
\]

**Solution:** \( x = -7, y = 10 \)  
Check: \( 81 \cdot (-7) + 57 \cdot 10 = -567 + 570 = 3 \) ✅

---

## **XIV. Linear Diophantine Equations**

**🔹 General form:** \( ax + by = c \)

**🔹 Solvability condition:** \( \gcd(a, b) \mid c \)

**🔹 Finding one solution:**
1. Find \( x_0, y_0 \) for \( ax + by = \gcd(a, b) \) using Extended Euclidean
2. Multiply by \( k = \frac{c}{\gcd(a, b)} \):  
   Particular solution: \( x_p = k \cdot x_0, y_p = k \cdot y_0 \)

**🔹 General solution:**
\[
x = x_p + \frac{b}{d} \cdot t, \quad y = y_p - \frac{a}{d} \cdot t
\]
where \( d = \gcd(a, b), t \in \mathbb{Z} \)

---

## **XV. Euler's Totient Theorem**

**🔹 Definition:** \( \phi(n) \) = count of integers ≤ n that are coprime to n

**🔹 Formula:** For \( n = p_1^{k_1}p_2^{k_2}\dots \)
\[
\phi(n) = n \left(1 - \frac{1}{p_1}\right)\left(1 - \frac{1}{p_2}\right)\dots
\]

**🔹 Theorem:** If \( \gcd(a, n) = 1 \), then  
\( a^{\phi(n)} \equiv 1 \pmod{n} \)

**Example:** Find \( 7^{100} \mod 24 \)

- \( \phi(24) = 24 \cdot (1 - \frac{1}{2})(1 - \frac{1}{3}) = 24 \cdot \frac{1}{2} \cdot \frac{2}{3} = 8 \)
- Since \( \gcd(7, 24) = 1 \): \( 7^8 \equiv 1 \pmod{24} \)
- \( 7^{100} = 7^{8 \cdot 12 + 4} = (7^8)^{12} \cdot 7^4 \equiv 1^{12} \cdot 7^4 \pmod{24} \)
- \( 7^2 = 49 \equiv 1 \pmod{24} \), so \( 7^4 \equiv 1^2 = 1 \pmod{24} \)

**Answer:** 1

---

## **XVI. Stars and Bars Combinatorics**

**🔹 Theorem 1 (Non-negative solutions):**  
Number of solutions to \( x_1 + x_2 + \dots + x_k = n \) with \( x_i \geq 0 \):
\[
\binom{n + k - 1}{k - 1}
\]

**🔹 Theorem 2 (Positive solutions):**  
Number of solutions to \( x_1 + x_2 + \dots + x_k = n \) with \( x_i \geq 1 \):
\[
\binom{n - 1}{k - 1}
\]

**Example:** Distribute 10 identical candies to 4 children, each gets ≥ 1 candy.

- \( x_1 + x_2 + x_3 + x_4 = 10, x_i \geq 1 \)
- **Theorem 2:** \( \binom{10 - 1}{4 - 1} = \binom{9}{3} = 84 \)

---

## **XVII. Matrix Exponentiation for Recurrences**

**🔹 Technique:** Express linear recurrence as matrix multiplication

**Example:** Fibonacci \( F_n = F_{n-1} + F_{n-2} \)

**Step 1 - Matrix form:**
\[
\begin{bmatrix} F_n \\ F_{n-1} \end{bmatrix} = 
\begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix} \cdot
\begin{bmatrix} F_{n-1} \\ F_{n-2} \end{bmatrix}
\]

**Step 2 - General formula:**
\[
\begin{bmatrix} F_n \\ F_{n-1} \end{bmatrix} = 
\begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}^{n-1} \cdot
\begin{bmatrix} F_1 \\ F_0 \end{bmatrix}
\]

**Step 3 - Compute \( M^{n-1} \) using binary exponentiation in \( O(\log n) \) time**

---

## **XVIII. Game Theory - Nim & Grundy Numbers**

**🔹 Nim Game:** Multiple piles, take any number from one pile

**🔹 Winning condition:** XOR of all pile sizes ≠ 0

**Example:** Piles [3, 4, 5]
- \( 3 \oplus 4 \oplus 5 = 011 \oplus 100 \oplus 101 = 010 = 2 \neq 0 \) → **First player wins**

**🔹 Grundy Numbers (for impartial games):**
- mex(S) = minimum excluded non-negative integer from set S
- Grundy(n) = mex{Grundy(all reachable positions from n)}
- **Composite game:** XOR of Grundy numbers of all games

---

## **XIX. Linearity of Expectation**

**🔹 Powerful principle:** \( E[X + Y] = E[X] + E[Y] \)  
**Even when X and Y are dependent!**

**Example:** Expected number of fixed points in random permutation of n elements.

Let \( X_i = 1 \) if element i in position i, else 0  
\( E[X_i] = P(\text{element i in position i}) = \frac{1}{n} \)  
By linearity: \( E[\sum X_i] = \sum E[X_i] = n \cdot \frac{1}{n} = 1 \)

**Answer:** Expected fixed points = 1 (regardless of n!)

---

## **XX. Mobius Inversion & Inclusion-Exclusion**

**🔹 Mobius function:**
\[
\mu(n) = 
\begin{cases}
1 & \text{if } n = 1 \\
(-1)^k & \text{if } n = p_1 p_2 \dots p_k \ (\text{distinct primes}) \\
0 & \text{if } p^2 \mid n
\end{cases}
\]

**🔹 Mobius inversion:**
If \( g(n) = \sum_{d \mid n} f(d) \), then  
\( f(n) = \sum_{d \mid n} \mu(d) g(\frac{n}{d}) \)

**Application:** Count numbers ≤ N coprime to N = \( \sum_{d \mid N} \mu(d) \cdot \frac{N}{d} \)

---

## **XXI. Fast Fourier Transform (Concept)**

**🔹 Purpose:** Multiply polynomials in \( O(n \log n) \) instead of \( O(n^2) \)

**🔹 Key insight:**
- **Evaluation:** Compute polynomial at 2n points → \( O(n \log n) \)
- **Point-wise multiplication** → \( O(n) \)
- **Interpolation:** Reconstruct product polynomial → \( O(n \log n) \)

**🔹 Uses:** Large integer multiplication, polynomial multiplication, convolution

---

## **Practice Problems to Internalize These Concepts:**

1. **Extended Euclidean:** Solve \( 56x + 72y = 8 \)
2. **Stars and Bars:** Count solutions to \( a + b + c = 15 \) with \( a \geq 2, b \geq 0, c \geq 3 \)
3. **Matrix exponentiation:** Find \( F_{20} \) for \( F_n = 2F_{n-1} + 3F_{n-2} \)
4. **Game theory:** Find winning move for piles [5, 7, 9] in Nim
5. **Linearity of expectation:** Expected number of dice rolls to get all 6 faces

---

# 🧠 **Competitive Programming Equations Encyclopedia**
*Advanced Formulas & Techniques*

---

## **XXII. Advanced Modular Arithmetic**

### **1. Wilson's Theorem**
\[
(p-1)! \equiv -1 \pmod{p} \quad \text{for prime } p
\]

### **2. Lucas Theorem** (for binomial coefficients modulo prime)
\[
\binom{n}{k} \bmod p = \binom{\lfloor n/p \rfloor}{\lfloor k/p \rfloor} \cdot \binom{n \bmod p}{k \bmod p} \bmod p
\]

### **3. Chinese Remainder Theorem (General Form)**
Solve:
\[
\begin{cases}
x \equiv a_1 \pmod{m_1} \\
x \equiv a_2 \pmod{m_2} \\
\vdots \\
x \equiv a_k \pmod{m_k}
\end{cases}
\]

Solution exists if \( \gcd(m_i, m_j) \mid (a_i - a_j) \) for all i, j

---

## **XXIII. Combinatorics Deep Dive**

### **1. Derangements** (!n - permutations with no fixed points)
\[
!n = n! \sum_{k=0}^{n} \frac{(-1)^k}{k!} = \left\lfloor \frac{n!}{e} + \frac{1}{2} \right\rfloor
\]
\[
!n = (n-1)[!(n-1) + !(n-2)]
\]

### **2. Catalan Numbers** (multiple definitions)
\[
C_n = \frac{1}{n+1} \binom{2n}{n} = \binom{2n}{n} - \binom{2n}{n-1}
\]
\[
C_0 = 1, \quad C_{n+1} = \sum_{i=0}^{n} C_i C_{n-i}
\]

**Applications:** Valid parentheses, binary trees, polygon triangulations

### **3. Stirling Numbers**
- **First kind:** \( s(n,k) \) - permutations of n with k cycles
- **Second kind:** \( S(n,k) \) - partitions of n into k non-empty subsets
\[
S(n,k) = \frac{1}{k!} \sum_{j=0}^{k} (-1)^{k-j} \binom{k}{j} j^n
\]

### **4. Burnside's Lemma**
For group G acting on set X:
\[
\text{Number of orbits} = \frac{1}{|G|} \sum_{g \in G} |X^g|
\]
where \( X^g \) = elements fixed by g

---

## **XXIV. Probability & Expectation Advanced**

### **1. Variance Formula**
\[
\text{Var}(X) = E[X^2] - (E[X])^2
\]

### **2. Conditional Expectation**
\[
E[X] = E[E[X|Y]]
\]

### **3. Geometric Distribution**
Expected trials until success: \( E[X] = \frac{1}{p} \)

### **4. Markov Chains**
Stationary distribution π satisfies: \( \pi P = \pi \)

---

## **XXV. Linear Algebra for CP**

### **1. Matrix Determinant**
- **2×2:** \( \det \begin{bmatrix} a & b \\ c & d \end{bmatrix} = ad - bc \)
- **3×3:** Use Sarrus rule or cofactor expansion

### **2. Matrix Inverse**
\[
A^{-1} = \frac{1}{\det(A)} \text{adj}(A)
\]

### **3. Characteristic Polynomial**
For eigenvalue λ: \( \det(A - \lambda I) = 0 \)

### **4. Cayley-Hamilton Theorem**
Every matrix satisfies its own characteristic equation

---

## **XXVI. Number Theory Advanced**

### **1. Primitive Roots**
g is primitive root modulo p if: \( \{g^1, g^2, \dots, g^{p-1}\} \) covers all residues 1..p-1

Number of primitive roots modulo n: \( \phi(\phi(n)) \)

### **2. Discrete Logarithm**
Solve: \( a^x \equiv b \pmod{m} \)

**Baby-step giant-step:** \( O(\sqrt{m}) \) solution

### **3. Quadratic Residues**
Legendre symbol:
\[
\left(\frac{a}{p}\right) = 
\begin{cases}
1 & \text{a is QR modulo prime p} \\
-1 & \text{a is QNR} \\
0 & p \mid a
\end{cases}
\]

### **4. Tonelli-Shanks Algorithm**
Find x such that \( x^2 \equiv a \pmod{p} \) for prime p

---

## **XXVII. Computational Geometry Formulas**

### **1. Cross Product & Orientation**
\[
\text{cross}(p,q,r) = (q_x - p_x)(r_y - p_y) - (q_y - p_y)(r_x - p_x)
\]
- > 0: counterclockwise
- = 0: collinear  
- < 0: clockwise

### **2. Line Intersection**
For lines \( a_1x + b_1y + c_1 = 0 \) and \( a_2x + b_2y + c_2 = 0 \):
\[
x = \frac{b_1c_2 - b_2c_1}{a_1b_2 - a_2b_1}, \quad
y = \frac{a_2c_1 - a_1c_2}{a_1b_2 - a_2b_1}
\]

### **3. Convex Hull Area (Shoelace)**
\[
\text{Area} = \frac{1}{2} \left| \sum_{i=1}^{n} (x_i y_{i+1} - x_{i+1} y_i) \right|
\]

### **4. Point in Polygon**
Ray casting algorithm: odd intersections = inside, even = outside

---

## **XXVIII. String Algorithms Math**

### **1. Polynomial Rolling Hash**
\[
H(s) = \left( \sum_{i=0}^{n-1} s[i] \cdot p^i \right) \bmod m
\]
**Double hash:** Use two different (p, m) pairs

### **2. Knuth-Morris-Pratt (KMP)**
Failure function: \( \pi[i] \) = length of longest proper prefix that is also suffix

### **3. Z-Algorithm**
\( Z[i] \) = longest substring starting at i that is also prefix

---

## **XXIX. Advanced Data Structures Math**

### **1. Fenwick Tree Range Updates**
**Point query, range update:**
- Update [l, r] with +val:  
  \( add(l, val), add(r+1, -val) \)

**Range query, point update:** Standard

**Range query, range update:** Use two BITs

### **2. Segment Tree with Lazy Propagation**
**Mathematical formulation:**
- Combine function for nodes
- Apply function for lazy updates
- Merge function for lazy values

### **3. Sparse Table**
**Ideal for:** Range min/max/gcd queries (idempotent functions)
\[
\text{ST}[i][j] = f(\text{ST}[i][j-1], \text{ST}[i + 2^{j-1}][j-1])
\]

---

## **XXX. Optimization & DP Techniques**

### **1. Convex Hull Trick**
For DP of form: \( dp[i] = \min_{j<i} (m_j \cdot x_i + c_j) \)

Maintain lower hull of lines (m, c)

### **2. Divide & Conquer Optimization**
For DP: \( dp[i][j] = \min_{k<j} (dp[i-1][k] + C[k][j]) \)

If \( C \) satisfies quadrangle inequality:  
Optimal k is monotonic

### **3. Knuth Optimization**
Similar to D&C, for DP with cost function C[i][j]

---

## **XXXI. Game Theory Advanced**

### **1. Grundy Numbers (Sprague-Grundy)**
For game G = G₁ + G₂ + ... + Gₙ:
\[
\text{Grundy}(G) = \text{Grundy}(G_1) \oplus \text{Grundy}(G_2) \oplus \dots \oplus \text{Grundy}(G_n)
\]

### **2. Misère Nim**
Like normal Nim except:
- If all piles ≤ 1: winning if XOR = 0
- Else: same as normal Nim

### **3. Subtraction Games**
Grundy(n) = mex{Grundy(n - s) for s in S}  
where S = allowed moves

---

## **XXXII. Fast Computation Formulas**

### **1. Fast Exponentiation**
\[
a^n = 
\begin{cases}
1 & \text{if } n = 0 \\
(a^{n/2})^2 & \text{if } n \text{ even} \\
a \cdot a^{n-1} & \text{if } n \text{ odd}
\end{cases}
\]

### **2. Fast Fibonacci**
\[
F_{2k} = F_k(2F_{k+1} - F_k)
\]
\[
F_{2k+1} = F_{k+1}^2 + F_k^2
\]

### **3. Fast nCr Precomputation**
Using factorials and inverse factorials:
\[
\text{nCr} = \frac{\text{fact}[n] \cdot \text{invFact}[r] \cdot \text{invFact}[n-r] \bmod M}
\]

---

## **XXXIII. Special Sequences & Functions**

### **1. Partition Function** p(n)
Number of ways to write n as sum of positive integers

**Recurrence:** 
\[
p(n) = \sum_{k \neq 0} (-1)^{k+1} p\left(n - \frac{k(3k-1)}{2}\right)
\]

### **2. Euler's Pentagonal Number Theorem**
\[
\prod_{k=1}^{\infty} (1 - x^k) = \sum_{k=-\infty}^{\infty} (-1)^k x^{k(3k-1)/2}
\]

### **3. Bernoulli Numbers**
Generating function: \( \frac{x}{e^x - 1} = \sum_{n=0}^{\infty} B_n \frac{x^n}{n!} \)

---

## **Practice Problem Types:**

1. **Derangements:** !10 = ?
2. **Catalan Application:** Count binary trees with 5 nodes
3. **CRT:** Solve x ≡ 2 mod 3, x ≡ 3 mod 5, x ≡ 2 mod 7
4. **Game Theory:** Grundy number for pile of 15 with moves {1,3,4}
5. **Geometry:** Area of polygon with vertices (0,0), (4,0), (4,3), (0,3)
6. **Probability:** Expected rolls to get all 6 faces of a die
7. **Combinatorics:** Stirling numbers S(5,3) = ?

---

This comprehensive collection covers **95%+ of mathematical concepts** needed for competitive programming up to the highest levels. Master these through targeted practice!