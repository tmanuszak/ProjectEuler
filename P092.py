count = 0
for i in range(1, 10000000):
    number = i
    while number != 1 and number != 89:
        number = sum([int(str(number)[i]) ** 2 for i in range(len(str(number)))])
    if number == 89:
        count += 1
print(count)
