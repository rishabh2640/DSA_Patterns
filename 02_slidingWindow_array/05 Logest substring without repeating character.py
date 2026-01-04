# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without duplicate characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        low = 0
        res = -1
        dic = {}

        for high in range ( n ):
            dic[s[high]] = dic.get(s[high], 0 ) + 1
            k = high - low + 1

            while len(dic) < k: # if length of dic is equals then it will be the outcome which we required and if len(dic) > k, which is not possible because len(dic) can never exceed k which is current window length.
                dic[s[low]] -= 1

                if dic[s[low]] == 0:
                    del dic[s[low]]

                low += 1
                k = high - low + 1

            length = high - low + 1
            res = max(res, length)
        if res == -1:
            return 0
        else:
            return res

s = "abcabcbb"
sol = Solution()

print(sol.lengthOfLongestSubstring(s))


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         char_set = set()
#         left = 0
#         max_len = 0

#         for right in range(len(s)):
#             while s[right] in char_set:
#                 char_set.remove(s[left])
#                 left += 1
#             char_set.add(s[right])
#             max_len = max(max_len, right - left + 1)

#         return max_len


