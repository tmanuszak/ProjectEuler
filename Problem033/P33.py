from fractions import Fraction

numerators = []
denominators = []

for i in range(1,10):
    for j in range(1,10):
        one = str(i)
        two = str(j)

        # check ones cancel
        for four in range(j + 1, 10):
            three = one
            if int(one + two) / int(three + str(four)) == int(one) / int(three) and int(one) / int(three) < 1:
                numerators.append(int(one + two))
                denominators.append(int(three + int(four)))

        # check tens cancel
        for three in range(i + 1,10):
            four = two
            if int(one + two) / int(str(three) + four) == int(two) / int(four) and int(two) / int(four) < 1:
                numerators.append(int(one + two))
                denominators.append(int(str(three) + four))

        # check \ cancel
        for three in range(1, 10):
            four = one
            if int(one + two) / int(str(three) + four) == int(two) / three and int(two) / three < 1:
                numerators.append(int(one + two))
                denominators.append(int(str(three) + four))

        # check / cancel
        for four in range(1, 10):
            three = two
            if int(one + two) / int(three + str(four)) == int(one) / four and int(one) / four < 1:
                numerators.append(int(one + two))
                denominators.append(int(three + str(four)))

bigNumerator = 1
for i in numerators:
    bigNumerator *= i

bigDenominator = 1
for i in denominators:
    bigDenominator *= i

print(Fraction(bigNumerator, bigDenominator))