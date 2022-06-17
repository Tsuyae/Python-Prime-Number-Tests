## Square Root Primality Test
## Noah Arevalo
import mpmath
import timeit
from mpmath import *

mp.dps = 30


def sqrtprimetest(n):

    isprime = True

    for i in range(2, int(floor(sqrt(n))+1)):
        print(i)
        if isint(fdiv(n,i)):            
            isprime = False
            break
    print(f"n={n}")
    print(isprime)
    



# start = timeit.default_timer()
# sqrtprimetest(394664667967121)
# stop = timeit.default_timer()
# print('Calculation Time: ', stop - start)

print(sqrt(394664667967121))


