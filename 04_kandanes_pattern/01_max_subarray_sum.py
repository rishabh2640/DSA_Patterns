# 53. Maximum Subarray

# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.


from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 0 
        bestend = nums[i]
        ans = nums[i]
        n = len(nums)

        for i in range(1,n):
            v1 = bestend + nums[i]
            v2 = nums[i]
            bestend = max(v1, v2)
            ans = max(ans, bestend)
        return ans

nums = [-2,1,-3,4,-1,2,1,-5,4]
solver = Solution()
print(solver.maxSubArray(nums))