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

def neighbors(M, j):
    return np.where(M[j] == 1)[0]

# non global (visited, parent) version of DFS
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


# Global version of DFS
visited1, parent1 = {},{}

def DFSInitGlobal(AMat):
    rows, cols = AMat.shape
    for i in range(rows):
        visited1[i] = False
        parent1[i] = -1
    return

def DFSGlobal(AMat, v):
    visited1[v] = True

    for k in neighbors(AMat, v):
        if not visited1[k]:
            k_int = int(k)
            parent1[k_int] = v
            DFSGlobal(AMat, k_int)
    return

DFSInitGlobal(adjacency_matrix); DFSGlobal(adjacency_matrix, 0);
print(visited1, parent1)


