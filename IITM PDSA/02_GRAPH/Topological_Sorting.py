# Directed Acyclic Graph (DAG) : Topological Sorting with Adjacency Matrix [taking Time complexity of O(n^2)]
import numpy as np
from myQueue import Queue

Adj_Mat = np.array([
    [0, 1, 1, 0],  # Node 0 goes to 1, 2
    [0, 0, 0, 1],  # Node 1 goes to 3
    [0, 0, 0, 1],  # Node 2 goes to 3
    [0, 0, 0, 0]   # Node 3 points to nothing
])

def topoSort(AMat):
    rows, cols = AMat.shape
    indegree = {}
    topoSortList = []

    for c in range(cols):
        indegree[c] = 0
        for r in range(rows):
            if AMat[r,c] == 1:
                indegree[c] = indegree[c] + 1
    
    for i in range(rows):
        j = min([k for k in range(cols) if indegree[k] == 0])
        topoSortList.append(j)
        indegree[j] = indegree[j] - 1

        for k in range(cols):
            if AMat[j,k] == 1:
                indegree[k] = indegree[k] - 1
    
    return topoSortList

print(topoSort(Adj_Mat))


# Directed Acyclic Graph (DAG) : Topological Sorting with Adjacency List [ Time complexity of O( m+n )]

adj_list = {
    0: [2, 3, 4],
    1: [3, 5],
    2: [4, 7],
    3: [5,],
    4: [6,],
    5: [6, 7],
    6: [],
    7: []
}
def topoSortAdjList(AList):
    indegree2, topoSortList2 = {}, []
    zeroDegreeQ = Queue()

    for i in AList.keys():
        indegree2[i] = 0

    for u in AList.keys():
        for v in AList[u]:
            indegree2[v] = indegree2[v] + 1
    
    for u in AList.keys():
        if indegree2[u] == 0:
            zeroDegreeQ.addq(u)
    
    while not zeroDegreeQ.isempty():
        j = zeroDegreeQ.delq()
        topoSortList2.append(j)
        indegree2[j] = indegree2[j] - 1

        for k in AList[j]:
            indegree2[k] = indegree2[k] - 1
            if indegree2[k] == 0:
                zeroDegreeQ.addq(k)
    return topoSortList2



print(topoSortAdjList(adj_list))

