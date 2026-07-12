# How it works: It divides the list into a "sorted" section and an "unsorted" section. It scans the entire unsorted section to find the absolute minimum value, and swaps it with the first unsorted element.Best 

# for: Situations where writing to memory is very expensive, because it performs the minimum possible number of swaps (at most $O(n)$ swaps).

# Key Trait: It scans the whole remaining list before making a single swap.

def selection_sort(arr):
    # store the length of the array
    n = len(arr)

    # Outer loop tracks boundary between sorted (left) and unsorted (right)
    for i in range(n):
        # assume the first element of the unsorted portion is the smallest
        min_idx = i

        # Iterate through the rest of the unsorted array to find the true minimum
        for j in range(i+1, n):

            # Compare the current element with the smallest element found so far
            if arr[j] < arr[min_idx]:
                # update the index of the minimum element if a smallest one is found
                min_idx = j
        
        # Swap the smallest found element with the first element of the unsorted portion
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

L = [3,4,2,7,9,1,8]
print(selection_sort(L))