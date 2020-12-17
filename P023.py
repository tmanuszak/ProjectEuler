from sympy import divisors
from itertools import combinations_with_replacement as comb
A = set(range(28123))
B = set(map(sum, comb((n for n in range(28123) if sum(divisors(n)[:-1]) > n), 2))) # Sum of abundant numbers set
print(sum(A.difference(B)))