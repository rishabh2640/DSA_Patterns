# 424. Longest Repeating Character Replacement

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.



class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        n = len( s )
        low = 0
        dic = {}
        res = 0
        
        for high in range( n ):

            dic[s[high]] = dic.get(s[high] , 0) + 1
            window = high - low + 1
            max_char = max(dic.values())
            diff = window - max_char

            while diff > k:
                dic[s[low]] -= 1
                if dic[s[low]] == 0:
                    del dic[s[low]]
                low += 1
                
                window = high - low + 1
                max_char = max(dic.values())
                diff = window - max_char
            
            window = high - low + 1
            res = max(res, window)
        
        return res

s = "AABABBA"
k = 1
sol = Solution()

print(sol.characterReplacement( s , k ))





# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         count = {}
#         res = 0
#         l = 0
#         max_f = 0  # Track the count of the most frequent char in the current window

#         for r in range(len(s)):
#             # Add current character to the count dictionary
#             count[s[r]] = count.get(s[r], 0) + 1
            
#             # Update the max frequency we've seen in the current window
#             max_f = max(max_f, count[s[r]])

#             # The condition: (Window Length) - (Count of Most Frequent Char) 
#             # tells us how many characters we need to replace.
#             # If that number is greater than k, our window is invalid.
#             while (r - l + 1) - max_f > k:
#                 count[s[l]] -= 1
#                 l += 1
            
#             # Update the result with the size of the valid window
#             res = max(res, r - l + 1)

#         return res
    
# s = "AABABBA"
# k = 1
# sol = Solution()

# print(sol.characterReplacement( s , k ))