# CS648
## Randomized Algorithms – Universal Hashing for O(1) Search

This project explores **universal hashing** as a randomized algorithm to achieve **expected constant-time (O(1)) search**.  
It combines **theory**, **mathematical proof**, and **implementation** to show how universal hashing outperforms traditional search algorithms like **binary search**, **binary search trees (BST)**, and **red-black trees**.

---

### 📖 Overview
Efficient searching is critical in computer science.  
While:
- **Binary Search** provides `O(log n)` performance (on sorted data),
- **Balanced Trees** (like Red-Black Trees) maintain `O(log n)` operations,  

**Universal Hashing** uses randomization to reduce collisions and achieve **expected O(1)** search time.

This project covers:
- **Why universal hashing is needed**  
- **Mathematical proof** of its constant-time expected search  
- **Implementation** for integer datasets  
- **Graphical performance comparison** with other search methods  

---

### 🔬 Theory in Brief

A family of hash functions \( \mathcal{H} \) is **universal** if for any two distinct keys \( x \neq y \):  

\[
\Pr_{h \in \mathcal{H}}[h(x) = h(y)] \leq \frac{1}{m}
\]

where \( m \) is the table size.  

This property ensures **low collision probability**, making the **expected search time**:  

\[
\mathbb{E}[T_{search}] = O(1)
\]
---

### ✨ Features
- **Mathematical Proof** – Formal derivation of O(1) expected search time  
- **Implementation** – Universal hashing for integers  
- **Comparison** – Binary Search, BST, and Red-Black Tree benchmarks  
- **Visualization** – Graphical performance analysis  

---

### 📊 Results
- Universal Hashing maintained **near-constant search time** even for large datasets.  
- BST and Red-Black Trees scaled logarithmically.  
- Binary Search lagged for large inputs.  
