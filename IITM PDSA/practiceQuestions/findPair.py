# Write a Python function findPair(L, pairSum) that return True if there exist a pair of integers in L whose sum is equal to x, False otherwise. Try to write a solution which is O(nlogn) or better.

# Hint: Try to sort the list first.

## For example, consider the below list. We need to find if there exists any pair whose sum is equal to 21. 11+10 = 21. So the function should return True.
## For the same list, if we want to find if there exist any pair whose sum is equal to 2. Clearly there is no such pair, so the function should return False.

# Sample Input 1
L = [10, 4, 11, 5, 1, 8, 7] 
pairSum = 21

# Output : True

def findPair(L, pairSum):
    L.sort()

    low = 0
    high = len(L) - 1

    while low < high:
        curr_elem = L[low] + L[high]

        if curr_elem == pairSum:
            return True
        elif curr_elem < pairSum:
            low += 1
        else:
            high -= 1
    return False

print( findPair(L, pairSum))