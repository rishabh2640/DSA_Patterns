# Prim's Algorithm Minimum shortest Tree

def primList(WList):
    visited, distance, TE = {},{},[]

    for i in WList.keys():
        visited[i], distance[i] = False, float('inf')

    visited[0] = True

    for v,d in WList[0]:
        distance[v] = d


    for i in range(1, len(WList.keys())):
        minDist = float('inf')
        nextV = None

        for u in WList.keys():
            for v,d in WList[u]:
                if visited[u] and not visited[v] and d < minDist:
                    nextV = v
                    minDist = d
                    nextE = (u,v)

        visited[nextV] = True
        TE.append(nextE)

        for v,d in WList[nextV]:
            if not visited[v]:
                if d < distance[v]:
                    distance[v] = d

    return TE

dEdges = [(0,1,10),(0,3,18),(1,2,20),(1,3,6),(2,4,8),(3,4,70)]
edges = dEdges + [(j,i,w) for (i,j,w) in dEdges]
size = 5
WL = {}
for i in range(size):
    WL[i] = []
for (i,j,d) in edges:
    WL[i].append((j,d))
print(primList(WL))