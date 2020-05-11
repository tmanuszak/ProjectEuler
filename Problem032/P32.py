pandigitalProducts = set()

def is_pan_mult(x, y):
    if sorted(str(x) + str(y) + str(x * y)) == list('123456789'):
        return x * y

for x in range(1, 100):
    for y in range(9999 // x):
        if is_pan_mult(x, y):
            pandigitalProducts.add(is_pan_mult(x, y))

print(sum(pandigitalProducts))