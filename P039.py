from sympy import gcd

pList = [0 for i in range(1001)]
m = 2
n = 1


def newtriple(x, y):
    return [x ** 2 - y ** 2, 2 * x * y, x ** 2 + y ** 2]


triple = newtriple(m, n)

while sum(triple) < 1001:
    while sum(triple) < 1001:
        k = 1
        while k * sum(triple) < 1001:
            pList[k * sum(triple)] += 1
            k += 1
        m += 1
        while gcd(m, n) != 1 or (m % 2 == 1 and n % 2 == 1):
            m += 1
        triple = newtriple(m, n)
    n += 1
    m = n + 1
    while gcd(m, n) != 1 or (m % 2 == 1 and n % 2 == 1):
        m += 1
    triple = newtriple(m, n)

largestNumberOfTriples = 0
perimeterWithMostTriples = 0
for i in range(len(pList)):
    if pList[i] > largestNumberOfTriples:
        largestNumberOfTriples = pList[i]
        perimeterWithMostTriples = i
print(perimeterWithMostTriples)
