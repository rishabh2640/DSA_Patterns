# Directed Acyclic Graph (DAG) : Topological Sorting with Adjacency Matrix [taking Time complexity of O(n^2)]
import numpy as np
Adj_Mat = np.array([
    [0, 1, 1, 0],  # Node 0 goes to 1, 2
    [0, 0, 0, 1],  # Node 1 goes to 3
    [0, 0, 0, 1],  # Node 2 goes to 3
    [0, 0, 0, 0]   # Node 3 points to nothing
])

def topoSort(AMat):
    rows, cols = AMat.shape
    indegree = {}
    toposort = []

    for c in range(cols):
        indegree[c] = 0
        for r in range(rows):
            if AMat[r,c] == 1:
                indegree[c] = indegree[c] + 1
    
    for i in range(rows):
        j = min([k for k in range(cols) if indegree[k] == 0])
        toposort.append(j)
        indegree[j] = indegree[j] - 1

        for k in range(cols):
            if AMat[j,k] == 1:
                indegree[k] = indegree[k] - 1
    
    return toposort

print(topoSort(Adj_Mat))