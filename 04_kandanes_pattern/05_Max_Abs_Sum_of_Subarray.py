# 1749. Maximum Absolute Sum of Any Subarray

# You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

# Return the maximum absolute sum of any (possibly empty) subarray of nums.

# Note that abs(x) is defined as follows:

# If x is a negative integer, then abs(x) = -x.
# If x is a non-negative integer, then abs(x) = x.

# Example 1:
# Input: nums = [1,-3,2,3,-4]
# Output: 5
# Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.

from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxEnd = nums[0]
        minEnd = nums[0]
        res = abs(nums[0])

        for i in range( 1, len(nums) ):

            maxEnd = max ( maxEnd + nums[i], nums[i] )            
            minEnd = min( minEnd + nums[i], nums[i] )

            res = max ( res, abs(maxEnd), abs(minEnd) )
        
        return res

# nums = [1,-3,2,3,-4]
nums = [-1]
solver = Solution()

print(solver.maxAbsoluteSum(nums))