import timeit
import mpmath
from mpmath import *



def F(n):
    mp.dps = ceil(log(factorial(n),10))
    return fdiv(mpf(factorial(n-1)+1), n)

def willans(n):
    if isint(F(n)):
        print(f"n={n}")
        print(isint(F(n)))
    else:
        print(f"n={n}")
        print(isint(F(n)))


start = timeit.default_timer()
willans(394664667967121)
stop = timeit.default_timer()
print('Calculation Time: ', stop - start)


#algo has to calculate (n-1)! which is n-1 operations
#but first, it has to calculate $log_10(n!) which is one operation