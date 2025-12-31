# 904. Fruit Into Baskets

# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.

# Example 1:
# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.

from typing import List

class Solution:

    def totalFruit(self, fruits: List[int]) -> int:
        n = len( fruits )
        dic = {}
        low = 0
        res = -1
        k = 2


        for high in range( n ): # iterating till high goes to length of array
            dic[ fruits[high] ] = dic.get( fruits[high] , 0 ) + 1

            while len(dic) > k:
                dic[ fruits[low] ] -= 1
                if dic[ fruits[low] ] == 0:
                    del dic[ fruits[low] ] 
                low += 1

            
            length = high - low + 1
            res = max(res, length)

        return res
    
fruits = [1,2,1]
sol = Solution()

print(sol.totalFruit(fruits))