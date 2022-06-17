#Python Application of AKS Algorithm
#by Noah Arevalo
import mpmath
import math
from mpmath import  *
import numpy as np


#perfPower weeds out any perfect powers.
def powerfree(n):
    for b in range(2, int(log(n,2))+1):
        a=root(n,b)
        if isint(a):
            return False
        else:
            return True

def phi(n):
    count = 0
    for i in range(1, n + 1):
        if math.gcd(n, i) == 1:
            count += 1 #adds 1 for each relatively prime number
    return count


#gcd(n,r) must be 1 here.
def ord(n,r):
    order = 0
    i=1
    if math.gcd(n,r) != 1 or r == 1:
        print("gcd(n,r) is not 1 or r=1. Please try again.")
        quit()
    while (n**i % r) != 1:
        i += 1
        if (n**i % r) == 1:
            break
    return i #add 1 to count last multiplication of n.


#by lemma 4.3 we know that there is an r =< max{3, ceil(log(n,n)**5)}
def rbound(n):
      bound = 3
      if bound < ceil(log(n,2)**5):
          bound = ceil(log(n,2)**5)
      return bound




def r(n):
    #declares list of coprime numbers that we are indexing by
    coprimenumbers = []
    for i in range(2, int(rbound(n)+1)):
        if math.gcd(n,i) == 1:
            coprimenumbers.append(i)

    for i in coprimenumbers:
        if ord(n,i) > log(n,2)**2:
            return i
            #here we find the smallest r for our given n
            #wikipedia states that r(31)= 29; this matches that

def nodivisorlessthanr(n):
    for i in range(2, r(n)+1):
        if 1<math.gcd(n,i)<n:
            return False
    return True
#print(nodivisorlessthanr(74513))
#first composite that passes this test


#if n gives a true value here, it means there is no such number a.
#it does not mean that n is prime.

def nleqr(n):
    if n <= r(n):
        return True
    else:
        return False
#this is the check in step 4 in the paper





#numpy stuff below

# A = np.poly1d([1,2])
# B = np.poly1d([4,9,5,4])
#
#
# quotient, remainder = np.polydiv(B, A)
#
# print(remainder)
# print(quotient)


# testpoly1 = [5]
# testpoly2 = [4,3,5,10,15]
# # #in adding we want to see [6,4]
# #
# # print(np.poly1d(testpoly1)-np.poly1d(testpoly2))
# #THIS WORKS. yields 6x + 4
#
# # print(np.poly1d(testpoly1)+6)
# #we ideally want [2,7]. aaaaaaand it works!
#
# quotient, remainder = np.polydiv(testpoly2, testpoly1)
#
#print(np.poly1d(np.polyadd(testpoly1, testpoly2)%5))
#should print [4,3,0,0,0]. it didnt. now it does!



#this function runs into its first rounding error when n = 17. :(
def fermat(n):
    for i in range(1, int(floor(sqrt(phi(r(n)))*log(n,2)))):
        leftpoly = np.array([1,i], dtype=object)
        #declares array from of (1X+a) in lieu of raising to nth power
        rightpoly = np.array([1,0], dtype=object)
        #declares (1X) in lieu of raising to nth power.
        #needs the zero for constant term =0
        lakspoly = (np.poly1d(leftpoly)**n)
        rakspoly = (np.poly1d(rightpoly)**n + i)
        rpoly = [1,0]
        ipoly = np.poly1d(rpoly)**r(n) - 1


        lrquotient, lrremainder = np.polydiv(lakspoly, ipoly)
        rrquotient, rrremainder = np.polydiv(rakspoly, ipoly)
        #we reduce each side of the congruence mod x^r - 1.

        lpolymodn = np.poly1d(np.array(lrremainder)%n)
        rpolymodn = np.poly1d(np.array(rrremainder)%n)


        #lnquotient, lnremainder = np.polydiv(lrremainder, npoly)
        #rnquotient, rnremainder = np.polydiv(rrremainder, npoly)
        #deprecated formula.
        #print(np.array(rakspoly))
        #np.array() turns the numpy polynomial back into an array


        # print(range(1, int(floor(sqrt(phi(n)*log(n,2))))+1))
        #print(np.poly1d(np.polyadd(np.array(lrremainder), [0])))
        #print(lrremainder == np.poly1d(np.polyadd(np.array(lrremainder), [0])%n))
        #checks that lrremainder is equal to its array. not eq mod n as expected

        ltestarray = np.array(lrremainder, dtype = object)
        #bugtesting
        # print(f"{r(n)}: r value for n = {n}")
        # print(f"{ipoly}: ideal polynomial of degree r(n)")
        # print(f"{lakspoly}: LHS akspoly")
        # print(f"{lrremainder}: LHS remainder when divided by the ideal")
        # print(f"{rrremainder}: RHS remainder when divided by the ideal")
        # print(f"{lpolymodn}:LHS remainder when div by ideal mod n")
        # print(f"{rpolymodn}:RHS remainder when div by ideal mod n")
        print(f"{ltestarray[28]}: constant term of array")
        print(i)
        print(i**31)
    
        
        
        if lpolymodn != rpolymodn:
            return False
        
        
        
        
        
    
        

          



        #print(f"{i} {lpolymodn == rpolymodn}")
        #return

        #WHAT WE KNOW -- when either side is divided by x^r - 1,
        #the greater the power, the greater the rounding error.
        #np.array(lrremainder) is incorrect
    return(True)








def aks(n):
    if not(powerfree(n) and nodivisorlessthanr(n)):
        return False
    #74513 is the first number that fails step 1 and 3


    if nleqr(n):
        return True

    
    if fermat(n):
        return True
    else:
        return False





def akstester(n): 
     for i in range(4,n):
         print(f"{aks(i)}, {i}")

def rtester(n): 
     for i in range(4,n):
         print(f"{r(i)}, {i}")



rtester(1000)




