x = 0
for i in range(1000):
    if i % 3 == 0:
        x += i
        continue
    elif i % 5 == 0:
        x += i