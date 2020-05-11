from sympy import nextprime, isprime

number = 11
truncatable = []
while len(truncatable) < 11:
    for i in range(len(str(number))):
        if isprime(int(str(number)[i+1:])) is False or isprime(int(str(number)[:-1-i])) is False:
            break
        elif i == len(str(number)) - 2:
            truncatable.append(number)
            break
    number = nextprime(number)

print(sum(truncatable))