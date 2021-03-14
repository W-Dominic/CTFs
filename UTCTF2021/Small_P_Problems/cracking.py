#Dominic Wojewodka
#3/14/2021
#UTCTF 2021

#for checking all the possible a's and b's 
#quadradic time complexity, very bad
def crack(p,g,A,B):
    a=1
    b=1
    while(a<A):
        a+=1
        b=0
        while(b<B):
            print()
            b1= (g**a)%p == A
            b2= (g**b)%p == B
            b3= (A**b)%p == (B**a)%p
            if(b1 and b2 and b3):
                return (A**b)%p
            else:
                b+=1
#checking all of the a's and b's isnt neccesary since we only need one to find s, the secret key
#thiis code checks all of the possible a's computes s and returns it
#linear time complexity
def crack2(p,g,A,B):
    i=1
    while(i<p):
        print(i)
        if((g**i)%p == A):
            a = i
            return (B**a)%p
        else:
            i += 1

#main
#for testing: should return 18
print(crack2(23,5,4,10))
#for the ctf
print(crack2(69691,1001,17016,47643))

