# Longest Substring with K Uniques

# You are given a string s consisting only lowercase alphabets and an integer k. Your task is to find the length of the longest substring that contains exactly k distinct characters.
# Note : If no such substring exists, return -1. 

# Examples:
# Input: s = "aabacbebebe", k = 3
# Output: 7
# Explanation: The longest substring with exactly 3 distinct characters is "cbebebe", which includes 'c', 'b', and 'e'.

class Solution:
    def longestKSubstr(self, s, k):
        # char = list( s )
        n = len( s )
        dic = {}
        low = 0
        res = -1

        for high in range( n ): # iterating till high goes till full length of array
            dic[ s[high] ] = dic.get( s[high] , 0 ) + 1 # increment the array value every time it sees the character

            while len(dic) > k: # while the length of dic extends the value k, then we have to correct the length of dic to back to k again in this loop
                dic[ s[low] ] -= 1 # firstly, decrement letter in eg. dic[s[0]=a] -=1 // a=3-1=2  
                if dic[ s[low] ] == 0: # if eg. dic[a] == 0, then remove the letter from dic 
                    del dic[ s[low] ] # deleting key value pair
                low += 1 # incrementing the low value to 1, next will be eg. dic[s[1]] -= 1 // where s[1] is also 'a' in a array, so in dic // a=2-1=1
            
            if len(dic) == k: # the moment length of dic == k
                length = high - low + 1 # calculate the length size of distinct character till now, from low to high
                res = max(res, length) # store the maximum result between res(result) and length

        if res == 0: 
            return -1 # store result -1 if there is no such string present
        else:
            return res

s = "aabacbebebe"
k = 3
sol = Solution()

print(sol.longestKSubstr(s,k))