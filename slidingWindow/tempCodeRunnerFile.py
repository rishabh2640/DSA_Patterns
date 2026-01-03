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