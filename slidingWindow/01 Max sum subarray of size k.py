# Max Sum Subarray of size K
# Difficulty: EasyAccuracy: 49.6%Submissions: 228K+Points: 2
# Given an array of integers arr[]  and a number k. Return the maximum sum of a subarray of size k.

# Note: A subarray is a contiguous part of any given array.

# Examples:

# Input: arr[] = [100, 200, 300, 400], k = 2
# Output: 700
# Explanation: arr2 + arr3 = 700, which is maximum.

class Solution:
    def maxSubarraySum(self, arr, k):
        low = 0
        high = k-1
        n = len(arr)
        sum = 0
        res = 0

        for i in range(high + 1):
            sum = sum + arr[i] #total sum of the sub array of k size
        
        while high<n:
            res = max(res, sum) #maximum of sum and res

            low += 1
            high +=1
            
            
            # sum = sum - arr[low-1] + arr[high]

            sum = sum - arr[low-1]

            if high == n:
                break

            sum = sum + arr[high]
        return res


arr = [100, 200, 300, 400]
k = 1
sol = Solution()

print(sol.maxSubarraySum(arr,k))
