import math
def solve():
    for a in range(1,500):
        for b in range(a,500):
            if a + b >= 1000:
                break
            elif math.sqrt(a**2 + b**2) % 1 == 0 and a + b + math.sqrt(a**2 + b**2) == 1000:
                return a * b * math.sqrt(a ** 2 + b ** 2)
print(solve())