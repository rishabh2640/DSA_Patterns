import numpy as np

adjacency_matrix = np.array([
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
])

AList = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2] 
}

# alternative using numpy
def neighbors(M, j):
    return np.where(M[j] == 1)[0]

def DFSInit(AMat):
    (rows, cols) = AMat.shape
    visited ,parent = {}, {}

    for i in range(rows):
        visited[i] = False
        parent[i] = -1
    
    return visited, parent

def DFS(AMat, visited, parent, v):
    visited[v] = True
    
    for k in neighbors(AMat, v):
        if not visited[k]:
            k_int = int(k)
            parent[k_int] = v
            visited,parent = DFS(AMat, visited, parent, k_int)
    return visited, parent

visited, parent = DFSInit(adjacency_matrix)
print(DFS(adjacency_matrix,visited, parent, 0 ))
