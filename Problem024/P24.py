from itertools import permutations as perm
print(list(perm([i for i in range(10)], 10))[999999])