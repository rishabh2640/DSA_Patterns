# func. takes non empty list of integers as input and returns a list [odd, even] , where odd is the sum of squares all the odd numbers in l and even is the sum of squares of all the even numbers in l.

L = [1,3,5]
L1 = [-1,-2,3,7]

def sumSquare(L):
    if not L:
        return

    odd = 0
    even = 0

    for i in range(len(L)):
        if L[i]%2 == 0:
            even = even + (L[i])**2
        else:
            odd = odd + (L[i])**2
    
    return [odd,even]

print(sumSquare(L))
print(sumSquare(L1))