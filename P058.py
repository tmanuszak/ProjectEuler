from sympy import isprime

index = 1
jump = 2
percent = 1
primes = 0
loops = 0
while percent > .1:
    for i in range(1, 5):
        index += jump
        if isprime(index):
            primes += 1
    loops += 1
    percent = primes / (4 * loops + 1)
    jump += 2
print(loops * 2 + 1)