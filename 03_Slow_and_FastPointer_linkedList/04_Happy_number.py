# 202. Happy Number

# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Example 1:
# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

# Example 2:
# Input: n = 2
# Output: false

# Constraints:
# 1 <= n <= 231 - 1

class Solution:
    def sumFun(self, n):
        sum = 0
        while n > 0:
            d = n % 10
            n //= 10
            sum = sum + d*d
        return sum

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n

        while fast != 1:
            slow = self.sumFun(slow)
            fast = self.sumFun(fast)
            fast = self.sumFun(fast)

            if slow == fast and slow != 1: #found cycle at other than 1
                return False
            
        return True #fast == 1

sol = Solution()
n = 19
print(sol.isHappy(n))


# class Solution:
#     def isHappy(self, n: int) -> bool:
#         def getNext(num):
#             res = 0
#             while num:
#                 last = num % 10
#                 res += last**2
#                 num //= 10
#             return res

#         slow = getNext(n)
#         fast = getNext(slow)
#         while slow != fast and slow != 1 and fast != 1:
#             slow = getNext(slow)
#             fast = getNext(getNext(fast))
#         return slow == 1 or fast == 1