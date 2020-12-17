def length_of_repeating_decimal(a, b):
    n = a % b
    if n == 0:
        return 0

    mem = {}
    n *= 10
    pos = 0

    while True:
        pos += 1
        n = n % b
        if n == 0:
            return 0
        if n in mem:
            i = mem[n]
            return pos - i
        else:
            mem[n] = pos
        n *= 10

longestLength = 0
denominator = 0
for i in range(1,1000):
    if length_of_repeating_decimal(1, i) > longestLength:
        longestLength = length_of_repeating_decimal(1, i)
        denominator = i
print(denominator)