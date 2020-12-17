import time
from decimal import *

start_time = time.time()

getcontext().prec = 102
print(sum([sum(Decimal(i).sqrt().as_tuple()[1][:100]) for i in range(2, 100) if round(i ** (1 / 2)) ** 2 != i]))

print("--- %s seconds ---" % (time.time() - start_time))