#Dominic Wojewodka
#03/19/2021
#UDCTF 2021
#PHEnomenal
import math
from decimal import *
getcontext().prec = 2000
def encrypt():
    
    c = Decimal(input("input c: "))
    m = Decimal(input("input m: "))
    n = math.sqrt(Decimal(input("input n^2")))
    print(n)

print(encrypt())

