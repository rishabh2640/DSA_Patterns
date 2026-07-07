# Long journey

# A tourist wants to travel around India from north to south. He has a policy that he never travels back towards the north. Write a Python function longJourney(AList) to find him a route with which he can visit the maximum number of cities according to his policy, where AList represents a graph of cities and routes between them. Every edge in adjacency list AList is a feasible route between one city to another from north to south. The function should return a list in the order the cities are to be visited to visit maximum cities.

AdjList = {'Madurai': ['Cochin', 'Kanyakumari'],
                'Vaishali': [],
                'Varanasi': ['Khajuraho', 'Bodhgaya'],
                'Thiruvanandhapuram': ['Kanyakumari'],
                'Udaipur': ['Gir', 'Ajanta'],
                'Rishikesh': ['Delhi'],
                'Shimla': ['Rishikesh'],
                'Bangalore': ['Chennai', 'Madurai'],
                'Agra': ['Ranthambore'],
                'Ellora': ['Aurangabad'],
                'Bodhgaya': ['Kolkatta'],
                'Cochin': ['Thiruvanandhapuram'],
                'Pushkar': ['Udaipur', 'Ranthambore'],
                'Ranthambore': ['Khajuraho'],
                'Gir': [],
                'Aurangabad': ['Mumbai'],
                'Kolkatta': ['Ajanta', 'Bangalore', 'Chennai'],
                'Chennai': ['Madurai'],
                'Sravasti': ['Kushinagar'],
                'Leh': ['Shimla'],
                'Sarnath': ['Varanasi'],
                'Delhi': ['Jaipur', 'Agra', 'Sravasti'],
                'Goa': ['Cochin', 'Bangalore'],
                'Kanyakumari': [],
                'Kushinagar': ['Sarnath', 'Vaishali'],
                'Khajuraho': ['Ajanta'],
                'Jaipur': ['Pushkar'],
                'Mumbai': ['Goa'],
                'Ajanta': ['Ellora', 'Aurangabad']
            }

def longJourney(AList):
    visited = set()
    finish_order = []

    def dfs(start):
        stack = [(start, iter(AList.get(start, [])))]
        visited.add(start)
        while stack:
            node, neighbors = stack[-1]
            advanced = False
            for nxt in neighbors:
                if nxt not in visited:
                    visited.add(nxt)
                    stack.append((nxt, iter(AList.get(nxt,[]))))
                    advanced = True
                    break
            if not advanced:
                finish_order.append(node)
                stack.pop()
    
    for city in AList:
        if city not in visited:
            dfs(city)
    
    topo_order = list(reversed(finish_order))

    dist = {city : 1 for city in AList}
    next_city = {city: None for city in AList}

    for city in reversed(topo_order):
        best_len , best_next = 0, None
        for neighbor in AList.get(city, []):
            if dist[neighbor] > best_len:
                best_len, best_next = dist[neighbor], neighbor
        
        if best_next is not None:
            dist[city] = 1 + best_len
            next_city[city] = best_next
    
    start_city = max(dist, key= dist.get)
    route = []
    current = start_city

    while current is not None:
        route.append(current)
        current = next_city[current]
    
    return route

print( longJourney(AdjList))


# another way using recursion

def longJourney(AList):
    memo = {}  # city -> best route (list of cities) starting from that city

    def longest_from(city):
        if city in memo:            # already solved this city before? reuse it
            return memo[city]

        best_route = [city]         # worst case: dead end, route is just this city
        for neighbour in AList.get(city, []):
            route = [city] + longest_from(neighbour)   # try going to this neighbour
            if len(route) > len(best_route):
                best_route = route                       # keep it if it's longer

        memo[city] = best_route
        return best_route

    # Try every city as a starting point, return whichever route is longest
    return max((longest_from(city) for city in AList), key=len)

# another way using recursion but little expended version

def longJourney(AList):
    """
    Function to find the longest path in a DAG (Directed Acyclic Graph).
    """
    # Memoization dictionary to store the longest possible path for each city
    memo = {}
    
    def dfs(city):
        # If the longest path for this city is already known, return it
        if city in memo:
            return memo[city]
            
        max_path = []
        # Traverse through neighboring cities
        for neighbor in AList.get(city, []):
            path = dfs(neighbor)
            # If the new path is longer than the old max_path, update it
            if len(path) > len(max_path):
                max_path = path
                
        # Add the current city to the start of the longest sub-path
        memo[city] = [city] + max_path
        return memo[city]
        
    longest_route = []
    
    # Check by considering every city in the graph as a starting point
    for city in AList:
        current_path = dfs(city)
        # Save the one with the longest route
        if len(current_path) > len(longest_route):
            longest_route = current_path
            
    return longest_route

