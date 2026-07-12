# How it works: It picks a "pivot" element from the array and partitions the other elements into two sub-arrays: those less than the pivot and those greater than the pivot. The sub-arrays are then sorted recursively.

# Best for: General-purpose sorting in most programming languages. When implemented well, it is typically faster in practice than Merge Sort.

# Key Trait: It sorts "in-place" (requiring very little extra memory) but its worst-case performance can be slow if a poor pivot is repeatedly chosen.

# quick sort is stable sorting and at worst case time complexity is O(n^2) [when list is already sorted, and pivot has been picked as min or max], but in average case it takes O(nlogn) TC, so, most of the cases, it works at it best, even better then merge sort

def partition(L, lower, upper):
    pivot = L[lower]
    i = lower

    for j in range(lower+1, upper +1):
        if L[j] <= pivot:
            i = i + 1
            L[j], L[i] = L[i], L[j]
    L[lower], L[i] = L[i], L[lower]
    return i

def quicksort(L, lower, upper):
    if lower < upper:
        pivot = partition(L, lower, upper)
        quicksort(L, lower, pivot-1)
        quicksort(L, pivot + 1, upper)    
    return L

L = [23 , 54 , 34, 76, 341, 12, 43]
print(quicksort(L, 0 , len(L)-1))