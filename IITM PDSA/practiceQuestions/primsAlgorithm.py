def FiberLink(distance_map):
    
    # 'visited' keeps track of cities already in the network.
    # 'distance' tracks the shortest cable length needed to connect a city to the network.
    # 'treeEdge' stores the actual pairs of cities connected.
    visited, distance, treeEdge = {}, {}, []
    
    # Variable to store our final answer (total cable length).
    minPathDist = 0

    # Iterate through every city. Mark them as False (unvisited).
    # Use float('inf') to represent infinity, meaning they are currently unreachable.
    for v in distance_map.keys():
        visited[v], distance[v] = False, float('inf')

    # Start the algorithm from the first city (index 0). 
    # Mark it as True because it's the starting point of our network.
    visited[0] = True
    
    # Look at all direct neighbors of city 0.
    # Update their 'distance' from infinity to the actual distance of the fiber line.
    for v, d in distance_map[0]:
        distance[v] = d

    # A spanning tree for V vertices always has exactly V - 1 edges.
    # This loop runs exactly that many times to build the complete network.
    for i in range(1, len(distance_map.keys())):
        
        # Reset minimum distance and next vertex trackers for this iteration.
        minDist = float('inf')
        nextV = None
        
        # THE SEARCH BLOCK
        # This nested loop scans every single edge in the entire graph.
        # It looks for an edge where the source 'u' is in the network (visited) 
        # and the destination 'v' is NOT in the network.
        # It keeps track of the absolute shortest edge that fits this criteria.
        for u in distance_map.keys():
            for v, d in distance_map[u]:
                if visited[u] and not visited[v] and d < minDist:
                    minDist = d
                    nextV = v
                    nextE = (u, v)
        
        # We found the best next city. 
        # Mark it as visited and add the edge to our MST record.
        visited[nextV] = True
        treeEdge.append(nextE)

        # UPDATE BLOCK
        # Now that 'nextV' is in the network, check all its neighbors.
        # If a neighbor is unvisited, and the connection from 'nextV' is shorter 
        # than its previously known best connection, update its 'distance'.
        for (v, d) in distance_map[nextV]:
            if not visited[v]:
                if d < distance[v]:
                    distance[v] = d

    # CALCULATION
    # The 'distance' dictionary now perfectly holds the weight of the specific 
    # fiber line used to connect each city to the network.
    # We iterate through it, ignoring any infinities, and sum it up.
    for u in distance_map.keys():
        if distance[u] != float('inf'):
            minPathDist = minPathDist + distance[u]

    return minPathDist