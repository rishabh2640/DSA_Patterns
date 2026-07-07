# Consider a system of n water tanks on a hill, connected via m pipes. Water can flow through these pipes only in one direction. We have a source of water that can be connected to only one of these water tanks. We need to find if there exists a master tank such that all the tanks in this group can be filled by connecting the water source to this master tank. The tanks are numbered from 1 to n.

# Write a Python function findMasterTank(tanks, pipes) that accepts arguments tanks which is a list of tanks, and pipes which is a list of tuples that represents connectivity through pipes, between tanks. Each tuple (i,j) in pipes represents a pipe such that, water can flow from tank i to tank j but not vice versa. Your function should find a master tank and return the number representing it, else should return 0 if no master tank exists in the system. If there are more than one master tank, return any one of them. Try to implement an algorithm that executes in linear time (O(n+m)O(n+m)).

v = [1, 2, 3, 4, 5, 6, 7]
numOfEdges = 9
e = [
    (1, 3),
    (2, 3),
    (3, 6),
    (4, 6),
    (4, 7),
    (6, 2),
    (7, 5),
    (5, 1),
    (5, 6)
]

def findMasterTank(tanks, pipes):
    if not tanks:
        return 0
    
    AList = {tank: [] for tank in tanks}
    for u,v in pipes:
        if u in AList:
            AList[u].append(v)
    
    from collections import deque

    visited = set()
    candidate = None

    for tank in tanks:
        if tank not in visited:
            q = deque([tank])
            candidate = tank
            visited.add(tank)

            while q:
                curr = q.popleft()
                for neighbor in AList[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)

    # verifying that this candidate tank actually reaches all tanks or not.
    visited.clear()
    q = deque([candidate])
    visited.add(candidate)

    while q:
        curr = q.popleft()
        for neighbor in AList[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
    
    if len(visited) == len(tanks): # this condition fails that means there is a disjoint component in it or there isn't any such tank
        return candidate
    
    return 0

print(findMasterTank(v,e))