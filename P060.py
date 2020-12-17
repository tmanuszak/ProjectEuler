import time
from sympy import sieve
from sympy.ntheory import isprime

start_time = time.time()
s = [i for i in sieve.primerange(0,10000)]
for a in range(1, len(s)):
    seta = set()
    for i in range(a + 1, len(s)):
        if isprime(int(str(s[a]) + str(s[i]))) and isprime(int(str(s[i]) + str(s[a]))):
            seta.add(s[i])
    lista = list(seta)
    lista.sort()

    if len(seta) > 0:
        for b in range(0, len(lista)):
            setb = set()
            for i in range(b + 1, len(lista)):
                if isprime(int(str(lista[b]) + str(lista[i]))) and isprime(int(str(lista[i]) + str(lista[b]))):
                    setb.add(lista[i])
            listb = list(setb)
            listb.sort()

            if len(setb) > 0:
                for c in range(0, len(listb)):
                    setc = set()
                    for i in range(c + 1, len(listb)):
                        if isprime(int(str(listb[c]) + str(listb[i]))) and isprime(int(str(listb[i]) + str(listb[c]))):
                            setc.add(listb[i])
                    listc = list(setc)
                    listc.sort()

                    if len(setc) > 0:
                        for d in range(0, len(listc)):
                            setd = set()
                            for i in range(d + 1, len(listc)):
                                if isprime(int(str(listc[d]) + str(listc[i]))) and isprime(int(str(listc[i]) + str(listc[d]))):
                                    setd.add(listc[i])

                            if len(setd) > 0:
                                z = seta.intersection(setb, setc, setd)
                                if len(z) > 0:
                                    x = list(z)
                                    x.sort()
                                    sum = s[a] + lista[b] + listb[c] + listc[d] + x[0]
                                    print(str(s[a]) + " + " + str(lista[b]) + " + " + str(listb[c]) + " + " + str(listc[d]) + " + " + str(x[0]) + " = " + str(sum))

print("--- %s seconds ---" % (time.time() - start_time))
