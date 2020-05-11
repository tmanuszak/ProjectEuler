sum = 1
for i in range(3,1002,2):
    sum += i**2
    for j in range(1,4):
        sum += i**2 - j * (i - 1)
print(sum)