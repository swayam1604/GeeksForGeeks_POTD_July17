# 💡 Power of K in Factorial of N – Python Solution

### 📌 Problem Statement

Given two positive integers `n` and `k`, determine the **maximum integer `x`** such that:

\[
k^x \text{ divides } n! \quad (\text{i.e., } n! \mod k^x = 0)
\]

---

### 🧠 Examples

#### ✅ Example 1:
**Input:**  
`n = 7`, `k = 2`  
**Output:**  
`4`  
**Explanation:**  
`7! = 5040`, and the highest power of `2` that divides `5040` is `2^4 = 16`.

#### ✅ Example 2:
**Input:**  
`n = 10`, `k = 9`  
**Output:**  
`2`  
**Explanation:**  
`10! = 3628800`, and the highest power of `9` that divides it is `9^2 = 81`.

---

### 🚀 Approach

1. **Prime Factorization of `k`**  
   Break `k` into its prime factors and store the exponent count of each prime.

2. **Count Prime Powers in `n!`**  
   Use Legendre’s formula to count how many times each prime factor of `k` appears in `n!`.

3. **Divide & Minimize**  
   For each prime factor `p` raised to power `e` in `k`, divide the count from `n!` by `e`.  
   The minimum across all such factors gives the answer.

---

### ✅ Python Solution

```python
class Solution:
    def maxKPower(self, n, k):
        def factorize(num):
            f = {}
            d = 2
            while d * d <= num:
                while num % d == 0:
                    f[d] = f.get(d, 0) + 1
                    num //= d
                d += 1
            if num > 1:
                f[num] = f.get(num, 0) + 1
            return f

        def count_in_fact(n, p):
            c = 0
            while n:
                n //= p
                c += n
            return c

        factors = factorize(k)
        res = float('inf')
        for p, pw in factors.items():
            res = min(res, count_in_fact(n, p) // pw)
        return res

Developed with 💻 by Swayam Sharma
