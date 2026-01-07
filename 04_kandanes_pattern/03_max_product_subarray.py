# 152. Maximum Product Subarray

# Given an integer array nums, find a subarray that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.
# Note that the product of an array with a single element is the value of that element.

# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        i = 0
        maxEnding = nums[i]
        minEnding = nums[i]
        res = nums[i]

        n = len(nums)

        for i in range(1,n):
            v1 = nums[i]
            v2 = maxEnding * nums[i]
            v3 = minEnding * nums[i]
            
            maxEnding = max(v1, v2, v3)
            minEnding = min(v1, v2, v3)
            res = max(res, maxEnding, minEnding)

        return res

solver = Solution()
nums = [-2,0,-1]

print(solver.maxProduct(nums))