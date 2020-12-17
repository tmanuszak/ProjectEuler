import math


def isPentagonal(number):
    if math.sqrt(24 * number + 1) % 6 == 5:
        return True
    else:
        return False


minDifference = 9999999999999999999999

pentNumbers = []
for i in range(1, 5000):
    pentNumbers.append((3 * i ** 2 - i) / 2)

for i in range(len(pentNumbers) - 1):
    for j in range(i + 1, len(pentNumbers)):
        if isPentagonal(abs(pentNumbers[i] + pentNumbers[j])) and isPentagonal(
                abs(pentNumbers[i] - pentNumbers[j])) and minDifference > abs(pentNumbers[i] - pentNumbers[j]):
            minDifference = abs(pentNumbers[i] - pentNumbers[j])

print(minDifference)
