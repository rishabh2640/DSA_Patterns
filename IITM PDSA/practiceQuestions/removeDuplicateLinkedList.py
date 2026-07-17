# Question is given in the Figure01.png

class Node:
    def __init__(self, data=None):
        self.data = data #stores data
        self.next = None # contains reference to the next node if it exists, otherwise None

#created Linked List which contains duplicate nodes
L = [1,1,2,2,3,3]
head = Node(L[0])
current = head
for data in L[1:]:
    current.next = Node(data)
    current = current.next

def removeDuplicate(head):
    recent = head

    while recent != None and recent.next != None:
        if recent.data == recent.next.data:
            recent.next = recent.next.next
        else:
            recent = recent.next
