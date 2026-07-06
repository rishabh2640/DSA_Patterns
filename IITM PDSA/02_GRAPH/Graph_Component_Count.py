# counting the components in a graph using BFS
from myQueue import Queue

AList = {
    0: [1],         # Component 1 (Vertices 0-1)
    1: [0], 
    2: [3, 4],      # Component 2 (Vertices 2-4)
    3: [2], 
    4: [2], 
    5: []           # Component 3 (Isolated vertex 5)
}

def BFSList(AList, v):
    visited = {}
    for i in AList.keys():
        visited[i] = False
    
    q = Queue()

    visited[v] = True
    q.addq(v)

    while not q.isempty():
        j = q.delq()
        for k in AList[j]:
            if not visited[k]:
                visited[k] = True
                q.addq(k)
    return visited

def Components(AList):
    component = {}
    for i in AList.keys():
        component[i] = -1
    
    comp_id, seen = 0, 0

    while seen <= max(AList.keys()):
        startV = min([i for i in AList.keys() if component[i] == -1])
        
        # creating a new visited list for unique components in a graph
        visited = BFSList(AList, startV)
        
        for i in visited.keys():
            if visited[i]:
                seen = seen + 1
                component[i] = comp_id
        comp_id = comp_id + 1
    
    return component

print("component count using BFS \n", Components(AList), "\n") # output of the components

# counting the components in a graph using DFS

AList2 = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2] 
}
visited2, pre, post = {},{},{}

def DFSInitPrePost(AList2):
    for i in AList2.keys():
        visited2[i] = False
        pre[i], post[i] = -1, -1
    return

def DFSPrePost(AList2, v, count):
    visited2[v] = True
    count = count + 1
    pre[v] = count
    for k in AList2[v]:
        if not visited2[k]:
            count = DFSPrePost(AList2, k, count)
    post[v] = count
    count = count + 1
    return count

DFSInitPrePost(AList2)
DFSPrePost(AList2, 0, 0)
print("DFS","\n","visited : ",visited2, "\n","pre : ", pre,"\n","post : ", post)
