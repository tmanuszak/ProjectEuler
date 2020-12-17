import math

factorials = [math.factorial(i) for i in range(10)]
print(sum([i for i in range(3,2309171) if sum([factorials[int(str(i)[j])] for j in range(len(str(i)))]) == i]))