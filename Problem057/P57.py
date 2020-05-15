from sympy import Integer


def list_to_frac(l):
    expr = Integer(0)
    for i in reversed(l[1:]):
        expr += i
        expr = 1/expr
    return l[0] + expr

M = [1]
count = 0
for i in range(1,1001):
    M.append(2)
    fraction = str(list_to_frac(M)).split("/")
    if len(fraction[0]) > len(fraction[1]):
        count += 1
print(count)