from sympy import Integer


def list_to_frac(l):
    expr = Integer(0)
    for i in reversed(l[1:]):
        expr += i
        expr = 1/expr
    return l[0] + expr

M = [2]
multiplier = 1
for i in range(1,100):
    if i % 3 == 2:
        M.append(2*multiplier)
        multiplier += 1
    if i % 3 != 2:
        M.append(1)
numerator = str(list_to_frac(M)).split("/")[0]
print(sum([int(numerator[i]) for i in range(len(numerator))]))