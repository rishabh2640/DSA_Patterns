# 141. Linked List Cycle

# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Example 1:
# linked list = 3 -> 2 -> 0 -> -4 -> 2
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:
# linked list = 1 -> 2 -> 1
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# Example 3:
# linked list = 1 -> null
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.



from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

solver = Solution()

# ==========================================
# Example 1: head = [3, 2, 0, -4], pos = 1
# ==========================================
print("--- Testing Example 1 ---")

# Step A: Create the nodes
node1 = ListNode(3)   # Index 0
node2 = ListNode(2)   # Index 1 (Cycle connects here)
node3 = ListNode(0)   # Index 2
node4 = ListNode(-4)  # Index 3 (Tail)

# Step B: Link them together (3 -> 2 -> 0 -> -4)
node1.next = node2
node2.next = node3
node3.next = node4

# Step C: Create the cycle (Connect Tail -> Index 1)
# The image shows -4 pointing back to 2
node4.next = node2  

# Step D: Run the solution
result1 = solver.hasCycle(node1)
print(f"Input: [3, 2, 0, -4], pos=1")
print(f"Has Cycle: {result1}")  # Expected: True
