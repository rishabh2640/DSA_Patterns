# 1186. Maximum Subarray Sum with One Deletion

# Given an array of integers, return the maximum sum for a non-empty subarray (contiguous elements) with at most one element deletion. In other words, you want to choose a subarray and optionally delete one element from it so that there is still at least one element left and the sum of the remaining elements is maximum possible.

# Note that the subarray needs to be non-empty after deleting one element.


# Example 1:
# Input: arr = [1,-2,0,3]
# Output: 4
# Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.

from typing import List

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        noDel = arr[0]
        oneDel = float('-inf')
        res = arr[0]

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        noDel = arr[0]
        oneDel = float('-inf')
        res = arr[0]

        for i in range( 1, len(arr) ):

            if oneDel == float( '-inf' ):
                v1 = arr[i]
            else:
                v1 = oneDel + arr[i]
            
            oneDel = max ( v1, noDel )

            noDel = max ( noDel + arr[i], arr[i] )

            res = max ( res, oneDel, noDel )
        
        return res

        # for i in range( 1, len(arr) ):

        #     prevNoDel = noDel
        #     prevOneDel = oneDel

        #     noDel = max ( noDel + arr[i], arr[i] )

        #     if prevOneDel == float( '-inf' ):
        #         v1 = arr[i]
        #     else:
        #         v1 = prevOneDel + arr[i]
            
        #     oneDel = max ( v1, prevNoDel )

        #     res = max ( res ,oneDel, noDel )
        
        # return res

solver = Solution()
# a = [1,-2,0,3]
a = [2,1,-2,-5,-2]

print(solver.maximumSum(a))
