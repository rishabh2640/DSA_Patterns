# Question is given in the Figure02.png

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.last = None

    def insert_end(self, data):
        newNode = Node(data)
        newNode.prev = self.last
        if self.head == None:
            self.head = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
    
    # for a given doubly_linked_list create one method:
    #### -> insert_at_pos(data.pos): that accepts as integer data and inserts it into the list at given pos position where 1 < pos <= len(list)

    def insert_at_pos(self,data,pos):
        newNode = Node(data)
        current = self.head

        for _ in range(1, pos-1):
            if current is not None:
                current = current.next
        
        if current is not None:
            newNode.next = current.next
            newNode.prev = current

            if current.next is not None:
                current.next.prev = newNode
            else:
                self.last = newNode
        
        current.next = newNode
