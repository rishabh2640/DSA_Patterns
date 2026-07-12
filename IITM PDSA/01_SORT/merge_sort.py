# How it works: It continuously divides the array in half until it cannot be divided further (single elements). Then, it repeatedly merges the smaller sub-lists back together in sorted order until there is only one sorted list remaining.

# Best for: Large datasets and linked lists. It guarantees a fast, consistent sorting time regardless of the initial order.

# Key Trait: It requires extra memory (space) to hold the temporary sub-lists during the merging process.

def merge_sort(arr):
    # Base case : if the array has 1 or 0 elements, it is already sorted
    if len(arr) <= 1:
        # Return the single-element array to halt recursion
        return arr
    # find the exact middle index of the array
    mid = len(arr) // 2

    # Recursively call merge_sort on the first half of the array
    left = merge_sort(arr[:mid])

    # Recursively call merge_sort on the second half of the array
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []

    # Initialize two pointers, 'i' for the left list and 'j' for the right list
    i = j = 0

    # Loop as long as both lists still have elements to compare
    while i < len(left) and j < right:
        if left[i] < right[j]:
            # If the left element is smaller, add it to the result list
            result.append(left[i])
            # Move the left pointer forward
            i += 1
        else:
            # If the right element is smaller (or equal) , add it to the result
            result.append(right[j])
            # Move the right pointer forward
            j += 1
    # Once one list is empty, dump any remaining items from the left list into the result
    result.extend(left[i:])
    # Dump any remaining items from the right list into the result
    # (Note: only one of these extend lines will actually add anything)
    result.extend(left[j:])

    return result
