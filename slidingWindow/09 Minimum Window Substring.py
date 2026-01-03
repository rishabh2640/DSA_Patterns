# 76. Minimum Window Substring

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.


# import sys

# class Solution:
#     # Helper function equivalent to your 'fun'
#     def fun(self, have, need):
#         for i in range(256):
#             if have[i] < need[i]:
#                 return False
#         return True

#     def minWindow(self, s: str, t: str) -> str:
#         n = len(s)
#         m = len(t)
        
#         # Initialize frequency lists for ASCII characters
#         have = [0] * 256
#         need = [0] * 256
        
#         if n < m:
#             return ""
            
#         # Fill the 'need' frequency array
#         for char in t:
#             need[ord(char)] += 1
            
#         low = 0
#         res_len = float('inf') # Python equivalent of INT_MAX
#         start = 0 # starting index start only from zero
        
#         # Main sliding window loop
#         for high in range(n):
#             # Expand window: Add current character to 'have'
#             have[ord(s[high])] += 1
            
#             # Shrink window: While constraints are met (jab tk sahi hai)
#             while self.fun(have, need):
#                 current_len = high - low + 1
                
#                 # Update result if we found a smaller window
#                 if res_len > current_len:
#                     res_len = current_len
#                     start = low
                
#                 # Remove character at 'low' and move pointer forward
#                 have[ord(s[low])] -= 1
#                 low += 1
                
#         if res_len == float('inf'):
#             return ""
            
#         # Return the substring
#         return s[start : start + res_len]

# s = "ADOBECODEBANC"
# t = "ABC"
# sol = Solution()
# print( sol.minWindow( s, t )) # output = "BANC"

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # Frequency map for characters in t
        need = [0] * 128  # 128 is enough for standard ASCII
        for char in t:
            need[ord(char)] += 1

        have = [0] * 128
        
        # 'required' tracks how many unique characters we still need to satisfy
        # We count total required characters from t
        required = len(t)
        
        min_len = float('inf')
        start_index = 0
        
        low = 0
        
        for high in range(len(s)):
            # Add character s[high] to our window
            curr_char = ord(s[high])
            if need[curr_char] > 0:
                if have[curr_char] < need[curr_char]:
                    required -= 1
            have[curr_char] += 1

            # While window is valid (required == 0), try to shrink it
            while required == 0:
                current_window_len = high - low + 1
                
                # Update minimum window if this one is smaller
                if current_window_len < min_len:
                    min_len = current_window_len
                    start_index = low
                
                # Shrink: Remove character s[low] from window
                left_char = ord(s[low])
                have[left_char] -= 1
                
                # If we removed a needed character, update required count
                if need[left_char] > 0 and have[left_char] < need[left_char]:
                    required += 1
                    
                low += 1

        return "" if min_len == float('inf') else s[start_index : start_index + min_len]


s = "ADOBECODEBANC"
t = "ABC"
sol = Solution()
print( sol.minWindow( s, t )) # output = "BANC"