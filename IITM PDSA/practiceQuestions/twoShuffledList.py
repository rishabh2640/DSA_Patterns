# Write a function shuffle(l1,l2) that takes two lists, l1 and l2 as input, and returns a list consisting of the first element in l1, then the first element in l2, then the second element in l1, then the second element in l2, and so on. If the two lists are not of equal length, the remaining elements of the longer list are appended at the end of the shuffled output.

# Sample Input
l1 = [0,2,4]
l2 = [1,3,5]

# Output
# [0, 1, 2, 3, 4, 5]

def shuffle(l1,l2):
    shuffled = []

    minLen = min(len(l1), len(l2))

    for i in range(minLen):
        shuffled.append(l1[i])
        shuffled.append(l2[i])

    shuffled.extend(l1[minLen:])
    shuffled.extend(l2[minLen:])

    return shuffled

print(shuffle(l1,l2))
