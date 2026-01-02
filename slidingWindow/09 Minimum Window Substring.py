# 76. Minimum Window Substring

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.


class Solution:
    def equal(self,have, need):
        for i in range(256):
            if have[i] < need[i]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        have = [0] * 256
        need = [0] * 256

        for char in t:
            need[ord(char)] += 1
        
        n = len(s)
        m = len(t)

        if n < m:
            return ""
        
        low = 0
        result = float('inf')
        start = -1

        for high in range( n ):
            have[ord(s[high])] += 1

            while self.equal(have, need):
                cur_window = high - low + 1
                if result > cur_window:
                    result = min(result, cur_window) 
                start = low

                have[ord(s[low])] -= 1
                low += 1

        if result == float('inf'):
            return ""

        return s[start: start + result]

s = "ADOBECODEBANC"
t = "ABC"
sol = Solution()
print( sol.minWindow( s, t )) # output = "BANC"




# import sys

# class Solution:
#     # Helper function equivalent to your 'fun'
#     def fun(self, have, need):
#         for i in range(256):
#             if have[i] < need[i]:
#                 return False
#         return True

    # def minWindow(self, s: str, t: str) -> str:
    #     n = len(s)
    #     m = len(t)
        
    #     # Initialize frequency lists for ASCII characters
    #     have = [0] * 256
    #     need = [0] * 256
        
    #     if n < m:
    #         return ""
            
    #     # Fill the 'need' frequency array
    #     for char in t:
    #         need[ord(char)] += 1
            
    #     low = 0
    #     res_len = float('inf') # Python equivalent of INT_MAX
    #     start = -1
        
    #     # Main sliding window loop
    #     for high in range(n):
    #         # Expand window: Add current character to 'have'
    #         have[ord(s[high])] += 1
            
    #         # Shrink window: While constraints are met (jab tk sahi hai)
    #         while self.fun(have, need):
    #             current_len = high - low + 1
                
    #             # Update result if we found a smaller window
    #             if res_len > current_len:
    #                 res_len = current_len
    #                 start = low
                
    #             # Remove character at 'low' and move pointer forward
    #             have[ord(s[low])] -= 1
    #             low += 1
                
    #     if res_len == float('inf'):
    #         return ""
            
    #     # Return the substring
    #     return s[start : start + res_len]