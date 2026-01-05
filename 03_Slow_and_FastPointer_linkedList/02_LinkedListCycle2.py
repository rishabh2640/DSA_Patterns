# 142. Linked List Cycle II

# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

# Do not modify the linked list.

# Example 1:
# Input: head = [3,2,0,-4], pos = 1 // 3->2->9->(-4)->2
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.





# Definition for singly-linked list.

# from typing import Optional
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#     def index(self, index):
#         current = self.head

# class Solution:

#     def find_index(self, head, target):
#             current = head
#             index = 0

#             while current:
#                 if current.val == target:
#                     return index
                
#                 current = current.next
#                 index += 1
            
#             return -1


#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

#         if head is None and head.next is None:
#             return "no cycle"
        
#         slow = head
#         fast = head

#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             print(slow.val)
#             print(fast.val)

#             if slow == fast:
#                 slow = head
#                 print(slow.val)
                
#                 while slow != fast:
#                     slow = slow.next
#                     print(slow)
#                     fast = fast.next
#                     print(fast)
#                     if slow == fast:
#                         finder = Solution()
#                         return f"The tail of the cycle is on the index {finder.find_index(head, slow.val)}"

# solver = Solution()

# node1 = ListNode(3)
# node2 = ListNode(2)
# node3 = ListNode(0)
# node4 = ListNode(-4)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node2 # cycle back to index 1

# print(solver.detectCycle(node1))


from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def index(self, index):
        current = self.head


# def find_index(self, head, target):
#         current = head
#         index = 0

#         while current:
#             if current.val == target:
#                 return index
            
#             current = current.next
#             index += 1
#         
#         return -1

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = head
                
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow

        return None

solver = Solution()

node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2 # cycle back to index 1

print(solver.detectCycle(node1))

