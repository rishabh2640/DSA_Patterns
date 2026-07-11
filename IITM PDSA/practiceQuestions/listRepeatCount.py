#"Write a Python function histogram(l) that takes as input a list of integers with repetitions and returns a list of pairs as follows:.

## -- for each number n that appears in l, there should be exactly one pair (n,r) in the list returned by the function, where r is the number of repetitions of n in l.

## -- the final list should be sorted in ascending order by r, the number of repetitions. For numbers that occur with the same number of repetitions, arrange the pairs in ascending order of the value of the number."

# Sample 1
L1 = [13, 12, 11, 13, 14, 13, 7, 7, 13, 14, 12]
# Output: [(11, 1), (7, 2), (12, 2), (14, 2), (13, 4)]

# Sample 2
L2 = [13, 7, 12, 7, 11, 13, 14, 13, 7, 11, 13, 14, 12, 14, 14, 7]
# Output: [(11, 2), (12, 2), (7, 4), (13, 4), (14, 4)]

def histogram(L):

    elements = {}
    for i in range(len(L)):
        elements[L[i]] = elements.get(L[i], 0) + 1
    print(elements)

    countList = sorted(elements.items(), key= lambda item : (item[1],item[0]))
    
    return countList


print(histogram(L2))