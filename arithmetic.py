import random
import sys
def gcd_extended(a,n):
    if (n>a):
        return gcd_extended(n,a)
    if (n==0):
        return [1,0]
    if (a%n==0):
        return [0,1]
    [x,y]=gcd_extended(n,a%n)
    return [y,x-(a//n)*y] 

def inv(a,n): #calculates a^-1 mod n
    [x,y]=gcd_extended(n,a%n)
    return y%n

def gcd(a,b):
    if (b>a):
        return gcd(b,a)
    if (b==0):
        return a
    if (a%b==0):
        return b
    return gcd(b,a%b)
def fast_exp(a,b,n):
    if (b==0):
        return 1
    elif (b%2==0):
        return fast_exp((a*a)%n,b//2,n)
    else :
        return (a*(fast_exp((a*a)%n,b//2,n)))%n
def random_primes(): #generates random prime upto 10**300 density if about 0.0014
    while True:
        p=random.randint(10**200,10**300-1)
        n=0
        while True:
            a=random.randint(1,p)
            if (fast_exp(a,p-1,p)==1):
                n+=1
            else :
                n=-1
                break
            if (n==50):
                break
        if (n==50):
            return p

