# you have a deck of shuffled cards ranging from 0 to 100000000. There are 2 sub-ordinate below you and two subordinates below them and it goes on.

## The of job of sub-ord. is to split the deck of cards that they received and give it to two sub-ord of them. If they receive a deck of cards from their subordinates, they merge it in an ascending order and give it their higher level.
## If a subOrd received only two card, then he/she himself/herself arrange in ascending order give it back that to the superior
## If a subOrd received only one card, then he/she will give back that to the superior.

# Your Task is to find how many people including you are received to sort the cards and print the sorted deck of cards and number of people required as tuple.

# Write a function def subordinates(L):

L = [10,33,45,67,92,100,5]
# Output : ([10, 10, 33, 33, 45, 45, 92], 7)

def subordinates(L):
    if len(L) == 1:
        return L, 1
    if len(L) == 2:
        if L[0] > L[1]:
            return [L[1], L[0]], 1
        else:
            return L, 1
    
    mid = len(L) // 2
    left_list, left_count = subordinates(L[:mid])
    right_list, right_count = subordinates(L[mid:])

    merged = []
    i = j = 0

    while i < len(left_list) and j < len(right_list):
        if L[i] < L[j]:
            merged.append(L[i])
            i += 1
        else: 
            merged.append(L[j])
            j += 1
    
    merged.extend(left_list[i:])
    merged.extend(right_list[j:])

    total_count = 1 + left_count + right_count

    return merged, total_count

print(subordinates(L))