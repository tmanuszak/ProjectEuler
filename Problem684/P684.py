from sympy import fibonacci

MOD = 1000000007


def S(k):
    n = k // 9
    r = (k % 9 + 2)

    return ((((r - 1) * r + 10) * pow(10, int(n), MOD) - 2 * (r + 9 * n + 4)) * pow(2, MOD - 2, MOD)) % MOD


total = 0
for i in range(2, 91):
    total += S(fibonacci(i))
    total = total % MOD

print(total % 1000000007)
