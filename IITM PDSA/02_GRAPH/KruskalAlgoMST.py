# Kruskal Algorithm Minimum shortest Tree

def kruskal(WList):
    edges, component, TE = [],{},[]

    edges = [(d,u,v) for u in WList.keys() for v,d in WList[u]]

    for u in WList.keys():
        component[u] = u

    edges.sort()

    for d,u,v in edges:
        if component[u] != component[v]: # no cycle found
            TE.append((u,v))
            c = component[u]

            for w in WList.keys():
                if component[w] == c:
                    component[w] = component[v]
    print(component)
    return TE





dEdges = [(0,1,10),(0,2,18),(1,2,6),(1,4,20),(2,3,70),(4,5,10),(4,6,10),(5,6,5)]
edges = dEdges + [(j,i,w) for (i,j,w) in dEdges]
size = 7
WL = {}
for i in range(size):
    WL[i] = []
for (i,j,d) in edges:
    WL[i].append((j,d))
print(kruskal(WL))