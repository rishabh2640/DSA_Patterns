# Consider a social network of friends/relatives, most of whom are closely connected. Visualize this as a graph where each vertex denotes a person, and if two people know each other there is an edge between the vertices denoting them. If persons x and y know each other directly, then there is an edge connecting x and y and level of connectivity between them is 1. If person x is a friend of person y and person y is friend of person z, but x is not a friend of z, then the level of connectivity between x and z is 2, and so on. The connectivity between people is always two way, i.e. if x directly knows y, then y also knows x directly.

# Complete the Python function findConnectionLevel(n, Gmat, Px, Py) that takes 4 arguments, number of persons n(n persons numbered from 0 to n-1), Gmat an adjacency matrix representation of n persons and their connections(if Gmat[x][y] = 1, then person x and yare directly connected), two persons Px and Py both numbers, and returns the minimum level of connectivity between Px and Py. Return 0 if Px and Py are not connected through anybody in the group.

n = 7
Gmat = [
[0,1,1,0,0,0,0],
[1,0,1,1,1,1,0],
[1,1,0,1,1,1,0],
[0,1,1,0,1,0,0],
[0,1,1,1,0,1,0],
[0,1,1,0,1,0,1],
[0,0,0,0,0,1,0]
]
Px = 6
Py = 0

def findConnectionLevel(n, Gmat, Px, Py):
    if Px == Py:
        return 0
    
    from collections import deque

    que = deque([(Px, 0)]) # Que of curr_vertex and curr_level
    
    visited = set()
    visited.add(Px)

    while que:
        curr_person , curr_level = que.popleft()

        if curr_person == Py:
            return curr_level
        
        for neighbor in range(n):
            if Gmat[curr_person][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                que.append((neighbor, curr_level + 1))
    
    return 0

print(findConnectionLevel(n,Gmat, Px,Py))