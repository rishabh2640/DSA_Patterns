# How it works: It builds the final sorted array one item at a time. It takes the next unsorted element and scans backward through the sorted section to "insert" it into its correct position—much like how you might sort a hand of playing cards.

# Best for: Small datasets or lists that are already mostly sorted. In a nearly sorted list, Insertion Sort is incredibly fast.

# Key Trait: It shifts elements over one by one to make room for the inserted element.

def insertion_sort(arr):
    # Start at the second element (index 1) , assuming the first is a sorted list of length 1
    for i in range(1, len(arr)):

        # store the current element being evaluated
        curr_elem = arr[i]

        # set 'j' to the index immediately to the left of the curr_elem
        j = i - 1

        # Run backward through the sorted portion as long as we haven't hit the
        # start (j>=0) AND the elements are larger than our curr_elem
        while j>=0 and curr_elem < arr[j]:

            # shift the larger element one position to the right to make room
            arr[j + 1] = arr[j]

            # Move our pointer one step further left to keep checking
            j -= 1

        # Once we find an element smaller than the key (or hit the start)
        # drop the key into the empty slot we created
        arr[j+1] = curr_elem
    
    return arr

L = [9,2,8,6]
print(insertion_sort(L))
