# Write a function Findpeak(L) that accepts a list L of n distinct elements and returns the peak element of the list. A list element is a peak if it is greater than its neighbors. For corner elements, we need to consider only one neighbor. Write an efficient solution of O(logn) complexity. Consider that there is only one peak is in the list, L.

# Sample Input 1
L = [5, 10, 20, 15]
# Output
# 20


def FindPeak(L):
    low = 0
    high = len(L) - 1

    while low <= high:
        mid = (low + high) // 2
        rightHigh = (mid == len(L)-1) or (L[mid] > L[mid+1])
        leftHigh = (mid == 0) or (L[mid] > L[mid-1])

        if rightHigh and leftHigh:
            return L[mid]
        elif not rightHigh:
            low = mid + 1
        else:
            high = mid - 1

print(FindPeak(L))