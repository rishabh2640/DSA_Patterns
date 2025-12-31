# 209. Minimum Size Subarray Sum

# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

class Solution:
    from typing import List
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = 0 
        high = 0
        sum = 0
        res = float('inf')
        minLen = 0
        n = len(nums)

        while high < n:
            sum = sum + nums[high] # hiring

            while sum >= target: # till target is fulfilled going, firing will occur

                minLen = high - low + 1 # storing the current sub array length
                res = min(res, minLen) # storing minimum length of sub array need to meet target

                sum = sum - nums[low] # firing low'th element
                low +=1 # incrementing low to next

            high+=1

        if res == float('inf') or res == 0:
            return 0
        else:
            return res

target = 11
nums = [1,1,1,1,1,1,1,1]
sol = Solution()

print(sol.minSubArrayLen(target, nums))

# time complexity = O(n)
# space complexity = O(1)

