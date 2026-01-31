# 918. Maximum Sum Circular Subarray

# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
# A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].
# A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

# Example 1:
# Input: nums = [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3.

from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        bestMax = nums[0]
        bestMin = nums[0]
        totalSum = nums[0]
        res1 = nums[0]
        ans = nums[0]
        res2 = nums[0]

        for i in range( 1, len(nums) ):
            v1 = nums[i]
            v2 = nums[i] + bestMax

            bestMax = max ( v1, v2 )
            res1 = max ( res1, bestMax )
        
        for i in range ( 1 , len(nums) ):
            v3 = nums[i]
            v4 = nums[i] + bestMin

            bestMin = min ( v3, v4 )
            ans = min(ans, bestMin)
            totalSum = totalSum + nums[i]

            res2 = totalSum - ans

        print(res1, res2)
        
        return res1 if res2 == 0 else max(res1, res2)

# arr = [1,-2,3,-2] #3
# arr = [5,-3,5] #10
# arr = [-5,3,5] #8
arr = [-3,-2,-3] #-2

solver = Solution()

print (solver.maxSubarraySumCircular(arr))