maxSteps = 0
numberWithMaxSteps = 0

def collatz_steps(n):
    current_steps = 0
    number = n
    while number != 1:
        if number % 2 == 0:
            number /= 2
            current_steps += 1
        else:
            number = 3*number+1
            current_steps += 1
    if number == 1:
        return current_steps

for i in range(1,1000000):
    steps = collatz_steps(i)
    if steps > maxSteps:
        maxSteps = steps
        numberWithMaxSteps = i

print(numberWithMaxSteps)