from sympy import divisor_count

keepGoing = True
nthTriangleNumber = 1
while keepGoing:
    if divisor_count(int((nthTriangleNumber + 1)*nthTriangleNumber/2)) >= 500:
        break
    else:
        nthTriangleNumber += 1
print((nthTriangleNumber + 1)*nthTriangleNumber/2)