# Single source shortest path - using Bellman Ford algorithm 
# allows negative weight but not negative weighted cycles

def bellmanFord_list(WList, s):
    distance = {}
    for u in WList.keys():
        distance[u] = float('inf')
    distance[s] = 0

    for _ in WList.keys():
        for u in WList.keys():
            for v,d in WList[u]:
                if distance[v] > distance[u] + d:
                    distance[v] = distance[u] + d

    return distance


dEdges = [
    (0,1,10),
    (0,2,80),
    (1,2,6),
    (1,4,20),
    (2,3,70),
    (4,5,50),
    (4,6,5),
    (5,6,10),
]
size = 7
WL = {}
for i in range(size):
    WL[i] = []
for u,v,d in dEdges:
    WL[u].append((v,d))

print(WL)
print( bellmanFord_list(WL, 0))