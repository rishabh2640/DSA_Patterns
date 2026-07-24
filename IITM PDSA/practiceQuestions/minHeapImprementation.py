
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


# https://livinnector.github.io/live-py-tutor/#code=L%20%3D%20%5B%20%5B2,%205,%209%5D,%0A%20%20%20%20%5B5,%2023,%2067,%20212%5D,%0A%20%20%20%20%5B1,%2010,%2022%5D%5D%0A%20%20%20%20%0Aimport%20heapq%0A%0Adef%20mergeKLists%28L%29%3A%0A%20%20%20%20min_heap%20%3D%20%5B%5D%0A%20%20%20%20result%20%3D%20%5B%5D%0A%20%20%20%20%0A%20%20%20%20%23%201.%20Populate%20the%20initial%20heap%20with%20the%20first%20element%20of%20each%20list%0A%20%20%20%20for%20i%20in%20range%28len%28L%29%29%3A%0A%20%20%20%20%20%20%20%20if%20L%5Bi%5D%3A%20%23%20Ensure%20the%20list%20is%20not%20empty%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20Push%20a%20tuple%3A%20%28value,%20list_index,%20element_index%29%0A%20%20%20%20%20%20%20%20%20%20%20%20heapq.heappush%28min_heap,%20%28L%5Bi%5D%5B0%5D,%20i,%200%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%23%202.%20Extract%20the%20minimums%20and%20push%20the%20next%20elements%0A%20%20%20%20while%20min_heap%3A%0A%20%20%20%20%20%20%20%20val,%20list_idx,%20element_idx%20%3D%20heapq.heappop%28min_heap%29%0A%20%20%20%20%20%20%20%20result.append%28val%29%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%23%20If%20the%20list%20we%20just%20pulled%20from%20has%20more%20elements,%20push%20the%20next%20one%0A%20%20%20%20%20%20%20%20if%20element_idx%20%2B%201%20%3C%20len%28L%5Blist_idx%5D%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20next_val%20%3D%20L%5Blist_idx%5D%5Belement_idx%20%2B%201%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20heapq.heappush%28min_heap,%20%28next_val,%20list_idx,%20element_idx%20%2B%201%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20return%20result%0A%20%20%20%20%0Aprint%28mergeKLists%28L%29%29&cumulative=false&curInstr=12&heapPrimitives=false&mode=edit&origin=opt-live.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
