# Question is given in the Figure04.png

# list the path of stations to reach the destination

# --- Prefix Code (Provided in the image) ---
def BFSListPathLevel(AList, v):
    level, parent = {}, {}
    for i in AList.keys():
        level[i] = -1
        parent[i] = -1
    q = []
    
    level[v] = 0
    q.append(v)
    
    while len(q) > 0:
        j = q.pop(0)
        for k in AList[j]:
            if level[k] == -1:
                level[k] = level[j] + 1
                parent[k] = j
                q.append(k)
    return level, parent

# --- Solution Code ---
def minimumhops(AList, start, end):
    # Call the provided BFS function to get level and parent dictionaries starting from 'start'
    level, parent = BFSListPathLevel(AList, start)
    
    # Check if 'end' was never reached by BFS (level is still -1) and it isn't the start node itself
    if level[end] == -1 and start != end:
        # If unreachable, return a list containing only the start node as requested
        return [start]
        
    # Initialize an empty list to build our shortest path backwards
    path = []
    
    # Set a tracker variable 'curr' to start tracing back from the 'end' node
    curr = end
    
    # Loop continuously until we trace all the way back to the beginning 
    # (The parent of 'start' remains -1 as set in the prefix code initialization)
    while curr != -1:
        # Add the current node to our path list
        path.append(curr)
        # Update 'curr' to be its own parent, moving one step backwards up the path
        curr = parent[curr]
        
    # Since we built the path backwards from end to start, we reverse the list to fix the order
    path.reverse()
    
    # Return the final correctly ordered list representing the shortest path
    return path

# --- Suffix Code / Testing ---
if __name__ == "__main__":
    start = 8
    end = 7
    AList = {
        0: [8],
        8: [0, 9],
        1: [3, 5, 8],
        3: [1, 7, 2],
        5: [4],
        2: [8, 9],
        9: [1],
        7: [8],
        4: [2, 6],
        6: [9]
    }
    
    shortestpath = minimumhops(AList, start, end)
    print(shortestpath) 
    # Output: [8, 9, 1, 3, 7]