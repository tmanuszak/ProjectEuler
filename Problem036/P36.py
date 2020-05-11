print(sum([i for i in range(1, 1000000) if bin(i)[2:] == bin(i)[2:][::-1] and str(i) == str(i)[::-1]]))
