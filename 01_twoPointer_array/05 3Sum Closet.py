# 16. 3Sum Closest

# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

# Example 1:
# **Input**: nums = [-1,2,1,-4], target = 1
# **Output**: 2
# **Explanation**: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution:
    from typing import List
    
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort() 
        n=len(nums)
        result = 0
        maxDiff = float('inf')
        
        for i in range(0,n-2):

            left=i+1
            right=n-1
            
            while left<right:
                sum= nums[left]+nums[right]+nums[i]
                diff=abs(sum-target)

                if diff<maxDiff:
                    maxDiff=diff
                    result=sum

                if sum==target:
                    left+=1
                    right-=1
                elif sum<target:
                    left+=1
                else:
                    right-=1
        return result
    
sList= [-1,2,1,-4] 
sol= Solution()
target=1

print(sol.threeSumClosest(sList,target))

# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         nums.sort()
#         n = len(nums)
#         diff = float('inf')
#         res_sum = 0

#         for i in range(n - 2):
#             left = i + 1
#             right = n - 1

#             while left < right:
#                 total = nums[i] + nums[left] + nums[right]
#                 d = abs(target - total)

#                 if diff > d:
#                     diff = d
#                     res_sum = total

#                 if total == target:
#                     return res_sum

#                 if total < target:
#                     left += 1
#                 else:
#                     right -= 1

#         return res_sum