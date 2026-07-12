# How it works: It divides the list into a "sorted" section and an "unsorted" section. It scans the entire unsorted section to find the absolute minimum value, and swaps it with the first unsorted element.Best 

# for: Situations where writing to memory is very expensive, because it performs the minimum possible number of swaps (at most $O(n)$ swaps).

# Key Trait: It scans the whole remaining list before making a single swap.

