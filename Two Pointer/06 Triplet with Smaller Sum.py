# Triplets with Smaller Sum

# Given an array `arr[]` of distinct integers of size `n` and a value `sum`, the task is to find the count of triplets `(i, j, k)`, having `(i<j<k)` with the sum of `(arr[i] + arr[j] + arr[k])` smaller than the given value `sum`.

# **Example 1:**

# Input: n = 4, sum = 2, arr[] = {-2, 0, 1, 3}
# Output: 2
# Explanation: Below are triplets with sum less than 2 (-2, 0, 1) and (-2, 0, 3).


class Solution:    
    def countTriplets( self, n, sum, arr):
        arr.sort()
        result = 0
        
        for i in range ( n - 2 ):
            
            left = i + 1
            right = n - 1
            
            while left < right:
                tripSum = arr[i] + arr[left] + arr[right]
                
                if tripSum>=sum:
                    right-= 1
                else:
                    result = result + (right - left)
                    left+= 1
        return result
    
sum = 12
arr = [5, 1, 3, 4, 7] 
n = len(arr)
sol = Solution()

print(sol.countTriplets(n,sum,arr))