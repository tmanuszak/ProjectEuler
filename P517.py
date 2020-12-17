import math


def gFunction(a,x):
    if x < a:
        return 1
    else:
        return gFunction(a, x-1) + gFunction(a, x - a)

print(gFunction(math.sqrt(90), 90) % 1000000007)