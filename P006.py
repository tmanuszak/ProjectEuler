sumsq = 0
sqsum = (100*101/2)**2
for i in range(1,101):
    sumsq += i**2
print(sqsum - sumsq)
