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
