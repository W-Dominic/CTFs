#Dominic Wojewodka
#03/19/2021
#UDCTF 2021
#PHEnomenal
import math
from decimal import *

getcontext().prec = 20000

def encrypt():
    
    C = input("input c: ")
    M1 = input("input m1: ")
    M2 = input("input m2: ")
    N2 = input("input n^2: ")
    
    c = Decimal(C)
    m1 = Decimal(M1)
    m2 = Decimal(M2)
    n2 = Decimal(N2)
    
    k = math.floor(m2/m1)
    c2 = expMod(c,k,n2)
    
    return c2

#revursive algorithm for modular exponentiation
def expMod(base,exp,mod): 
      
    if (base == 0): 
        return 0
    if (exp == 0): 
        return 1
      
    y = 0
    if (exp % 2 == 0): 
        y = expMod(base, exp / 2, mod) 
        y = (y * y) % mod 
      
    else: 
        y = base % mod 
        y = (y * expMod(base, exp - 1,mod) % mod) % mod 
    return ((y + mod) % mod) 

def main():
    print(encrypt())
if __name__ == "__main__":
    main()
