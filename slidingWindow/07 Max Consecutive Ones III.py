# 1004. Max Consecutive Ones III

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# Example 1:
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

from typing import List
class Solution:

    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len( nums )
        low = 0
        dic = {1:0}
        res = 0
        max_char = -1
        
        for high in range( n ):

            dic[nums[high]] = dic.get(nums[high] , 0) + 1
            
            window = high - low + 1
            max_char = max(max_char, dic[1])
            diff = window - max_char

            while diff > k:
                dic[nums[low]] -= 1
                # if dic[nums[low]] == 0:
                #     del dic[nums[low]]
                low += 1
                
                window = high - low + 1
                max_char = max(max_char, dic[1])
                diff = window - max_char
            
            window = high - low + 1
            res = max(res, window)        
        return res

# nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# k = 3

nums = [1,1,1,0,0,0,1,1,1,1]
k = 0
sol = Solution()

print(sol.longestOnes(nums, k)) #output 10


# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
#         begin = 0
#         window_state = 0
#         result = 0

#         for end in range(len(nums)):
#             if nums[end] == 0:
#                 window_state += 1

#             while window_state > k:
#                 if nums[begin] == 0:
#                     window_state -= 1
#                 begin += 1
            
#             result = max(result, end - begin + 1)
        
#         return result