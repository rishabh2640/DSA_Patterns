# Smallest sum contiguous subarray

# Given an array arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the minimum sum and return its sum.

# Example 1:
# Input: arr[] = {3,-4, 2,-3,-1, 7,-5}
# Output: -6
# Explanation: sub-array which has smallest 
# sum among all the sub-array is {-4,2,-3,-1} = -6

class Solution:
    def smallestSumSubarray(self, A, N):
        i = 0 
        bestend = A[i]
        ans = A[i]

        for i in range(1,N):
            v1 = bestend + A[i]
            v2 = A[i]
            bestend = min(v1, v2)
            ans = min(ans, bestend)
        return ans

A = [3,-4, 2,-3,-1, 7,-5]
N = len(A)
solver = Solution()
print(solver.smallestSumSubarray(A, N))