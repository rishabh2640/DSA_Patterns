# Divide and Conquer

# Here we are finding the
# inversion(an inversion is just a pair of numbers that are in the wrong order) in list and count it.

# What is an Inversion?

# A pair of indexes (i, j) form an inversion.
# This happens if i < j (index i comes before index j) and list[i] > list[j] (the value at i is bigger than the value at j).
# A sorted list has zero inversions.

def mergeAndCount(A,B):
    (m,n) = (len(A), len(B))
    C,i,j,k,count = [], 0 ,0,0,0

    while k < m+n:
        if i == m:
            C.append(B[j])
            j,k = j+1, k+1
        elif j == n:
            C.append(A[i])
            i,k = i+1, k+1 
        elif A[i] < B[j]:
            C.append(A[i])
            i,k = i+1, k+1
        else:
            C.append(B[j])
            j,k,count = j+1, k+1, count+(m-i)
    
    return (C, count)

def sortAndCount(A): # this is exactly merge sort algo
    n = len(A)

    if n <= 1:
        return (A, 0)
    
    L, countL = sortAndCount(A[:n//2])
    R, countR = sortAndCount(A[n//2:])

    B, countB = mergeAndCount(L, R)

    return (B, countL + countR + countB)

L = [6,2,3,4,5,2,3,4,5,7,8,9,0]
print(sortAndCount(L))
