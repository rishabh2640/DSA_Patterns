# function takes a list of L as input and returns true if absolute difference between each adjacent pair of elements strictly increases.

L = [1,3,7,2,9]
L1 = [1,3,7,2,-3]

def expanding(L):
    if not L:
        return False
    
    prevDiff = 0

    for i in range(1, len(L)):
        diff = abs(L[i - 1] - L[i])
        if diff <= prevDiff:
            return False
        else:
            prevDiff = diff
    return True

print(expanding(L))
print(expanding(L1))