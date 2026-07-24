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

def Dijkstra_List(WList, s):
    visited, distance = {}, {}

    for v in WList.keys():
        visited[v], distance[v] = False, float('inf')

    distance[s] = 0

    for u in WList.keys():
        min_dist = min([distance[v] for v in WList.keys() if not visited[v]])
        nextV_list = [v for v in WList.keys() if (not visited[v]) and distance[v] == min_dist]

        nextV = min(nextV_list)
        visited[nextV] = True

        for v,d in WList[nextV]:
            if distance[v] > distance[nextV] + d:
                distance[v] = distance[nextV] + d

    return distance

print(Dijkstra_List(WL, 0))