# question is given in the Figure03.png

class Node:
    def __init__(self, data):
        self.data = data # Stores data
        self.next = None # Contains reference to the next node if it exists, otherwise None

def mergeSortedList(head1, head2):
    # Create a dummy node to act as the starting point of the merged list
    dummy = Node(0)
    # Tail will point to the last node in our newly merged list
    tail = dummy
    
    # Traverse both lists as long as neither is empty
    while head1 is not None and head2 is not None:
        # Compare the data of the current nodes of both lists
        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
            
        # Move the tail pointer forward
        tail = tail.next
        
    # If one of the lists is exhausted, attach the remaining nodes of the other list
    if head1 is not None:
        tail.next = head1
    else:
        tail.next = head2
        
    # Return the head of the merged list (skipping the dummy node)
    return dummy.next




