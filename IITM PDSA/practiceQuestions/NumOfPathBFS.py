# Question given in the Figure05.png

# --- Prefix code provided in the problem ---
def BFSListPath(AList, v):
    visited, parent = {}, {}
    for i in AList.keys():
        visited[i] = False
        parent[i] = -1
    q = []
    
    visited[v] = True
    q.append(v)
    
    while len(q) > 0:
        j = q.pop(0)
        for k in AList[j]:
            if not visited[k]:
                visited[k] = True
                parent[k] = j
                q.append(k)
    return visited, parent

# --- Solution code ---
def backandforth(AList, end1, end2):
    # Initialize a counter to keep track of the number of valid routes found
    count = 0
    
    # Start a loop that continues until no new paths can be found
    while True:
        # Use the provided BFS function to find paths starting from end1
        visited, parent = BFSListPath(AList, end1)
        
        # Check if end2 was reached during the BFS traversal
        if not visited.get(end2, False):
            # If end2 is not visited, no more routes exist, so break the loop
            break
            
        # If we reached here, a new route to end2 was successfully found
        count += 1
        
        # Start tracing the path backwards from end2
        curr = end2
        # Create a list to store the nodes of the current route
        path = []
        
        # Trace back using the parent dictionary until the start node (parent is -1)
        while curr != -1:
            # Append the current node to our path list
            path.append(curr)
            # Update current node to its parent to move backwards
            curr = parent[curr]
        
        # Reverse the path so it goes in the correct order from end1 to end2
        path.reverse()
        
        # Extract only the intermediate nodes (excluding the start and end nodes)
        # Slicing [1:-1] removes the first element (end1) and last element (end2)
        intermediate_nodes = set(path[1:-1])
        
        # Remove all intermediate nodes from the graph so they cannot be reused
        for node in intermediate_nodes:
            # Check if the node is a key in the adjacency list
            if node in AList:
                # Delete the node entirely from the adjacency list dictionary
                del AList[node]
                
        # We also must remove any connections to these deleted nodes from other nodes
        for key in AList:
            # Rebuild the neighbor list, keeping only nodes not in intermediate_nodes
            AList[key] = [x for x in AList[key] if x not in intermediate_nodes]
            
    # Finally, return the total count of distinct paths found
    return count

# --- Suffix code for testing the sample input ---
if __name__ == "__main__":
    AList = {
        0: [2, 3, 6],
        2: [0, 3, 4],
        3: [4, 2, 0, 1],
        6: [1, 5, 0],
        1: [3, 6, 5],
        4: [2, 3, 5],
        5: [1, 4, 6]
    }
    end1 = 0
    end2 = 1
    
    print(backandforth(AList, end1, end2)) 
    # Expected Output: 3