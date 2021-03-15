#Dominic Wojewodka
#03/14/2021
#UTCTF2021
def crack(p,g,A,B):
    a=1
    b=1
    while(a<A):
        a += 1
        b = 1
        while(b<B):
            b1 = (g**a)%p == A
            b2 = (g**b)%p == B
            b3 = (B**a)%p == (A**b)%p
            if(b1 and b2 and b3):
                s = (B**a)%p
                return (f"your secret is: {s}")
            else:
                b += 1
                print(a,b)
###Main
print(crack(23,5,10,4))
