from sympy import divisor_sigma, is_amicable

M = []
for i in range(2, 10000):
    if is_amicable(i, divisor_sigma(i, 1) - i) and i not in M:
        M.append(i)
        M.append(divisor_sigma(i, 1) - i)
print(sum(M))