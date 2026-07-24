class CustomMinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self.heapify_up(len(self.heap)-1)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        # store min value
        root = self.heap[0]

        # move last element to the root and heapify down
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)

        return root

    def heapify_up(self, index):
        parent_index = (index-1) //2

        # compare the value of the tuple at index 0
        if index > 0 and self.heap[index][0] < self.heap[parent_index][0]:
            # swap if the child is smaller than the parent
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.heapify_up(parent_index)

    def heapify_down(self, index):
        smallest = index
        left_child = 2*index + 1
        right_child = 2*index + 2

        if left_child < len(self.heap) and self.heap[left_child][0] < self.heap[smallest][0]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child][0] < self.heap[smallest][0]:
            smallest = right_child

        if smallest != index:
            self.heap[index], self.heap[smallest] =  self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)

    def is_empty(self):
        return len(self.heap) == 0


def mergeKList(L):
    heap = CustomMinHeap()
    result = []

    for i in range(len(L)):
        if L[i]:
            heap.insert(L[i][0], i , 0)

    while not heap.is_empty():
        val, list_index, element_index = heap.extract_min()
        result.append(val)

        if element_index + 1 < len(L[list_index]):
            next_val = L[list_index][element_index+1]
            heap.insert((next_val, list_index, element_index+ 1))

    return result