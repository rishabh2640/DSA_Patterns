# creating an queue class for queue operation in BFS
import numpy as np
class Queue:
    def __init__(self):
        self.queue = []
    
    def addq(self, v):
        self.queue.append(v)
    
    def delq(self):
        v = None
        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return v

    def isempty(self):
        return (self.queue == [])

    def __str__(self):
        return ( str(self.queue) )

# function test our Class Queue
# que = Queue()
# for i in range(3):
#     que.addq(i)
#     print(que)
# print(que.isempty())

# for j in range(3):
#     v = que.delq()
#     print(v, que)
# print(que.isempty())

def neighbors(M, j):
    OnesList = []
    for idx, val in enumerate(M[j]):
        if val == 1:
            OnesList.append(idx)
    return OnesList

# alternative using numpy
# def neighbors(M, j):
#     return np.where(M[j] == 1)[0]

adjacency_matrix = np.array([
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
])

def BFS(AMat, j):
    (rows,cols) = AMat.shape
    q = Queue()
    visited = {}
    
    for i in range(rows):
        visited[i] = False
    
    visited[j] = True
    q.addq(j)

    while not q.isempty():
        v = q.delq()
        for k in neighbors(AMat, v):
            if not visited[k]:
                visited[k] = True
                q.addq(k)
    return (visited)

print(BFS(adjacency_matrix,2))

## Tracking Parent while BFS

AList = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2] 
}

def BFS_parentTracking(AList, j):
    visited, parent = {}, {}

    for i in AList.keys():
        visited[i] = False
        parent[i] = -1

    qu = Queue()
    visited[j] = True
    
    qu.addq(j)

    while not qu.isempty():
        v = qu.delq()
        for k in AList[v]:
            if not visited[k]:
                visited[k] = True
                parent[k] = v
                qu.addq(k)
    return visited,parent

print(BFS_parentTracking(AList, 0))



def BFSListPathLevel(AList, j):
    level, parent = {}, {}
    for i in AList.keys():
        level[i] = -1
        parent[i] = -1
    
    que = Queue()
    level[j] = 0
    que.addq(j)

    while not que.isempty():
        v = que.delq()
        for k in AList[v]:
            if level[k] == -1:
                level[k] = level[v] + 1
                parent[k] = v
                que.addq(k)
    return level,parent

print(BFSListPathLevel(AList, 0))

