maxsum = 0
for a in range(2,100):
    for b in range(2,100):
        string = str(a**b)
        maxsum = max(maxsum, sum([int(string[i]) for i in range(len(string))]))
print(maxsum)