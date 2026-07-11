# write a function prime_function(m) that takes an integer m and returns true if m is prime product and false otherwise.
import math
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i ==  0:
            return False
    return True

def prime_function(m):
    if m <= 0:
        return False
    
    for i in range(2, int(math.sqrt(m))+1):
        if m % i == 0:
            j = m // i
            
            if isPrime(j) and isPrime(i):
                return True
        
    return False

print(prime_function(7))