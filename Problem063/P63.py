import math
count = 1
for a in range(2,10):
    b = 1
    while b == int(math.floor(math.log10(a**b)) + 1):
        count += 1
        b += 1
print(count)