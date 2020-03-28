import math

def gcd(a, b): 
  
    if (a == 0 or b == 0):
        return 0
      
    if (a == b):
        return a 

    if (a > b):  
        return gcd(a - b, b) 
              
    return gcd(a, b - a)

def are_coprime(a : int, b : int) -> bool:
    return (gcd(a,b)==1)

def prime_factors(n: int) -> list:

    res = []

    for i in range(2, n):
        if n%i==0:
            res.append(i)

    return res