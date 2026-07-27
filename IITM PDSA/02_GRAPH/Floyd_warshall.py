# detect negative cycles,dynamic programming, no guarantee of unique path

def floydWarshall(WMat):
    # Initialization
    (rows, cols, x) = WMat.shape
    SP = np.zeros(shape=(rows, cols, cols+1))

    for i in range(rows):
        for j in range(cols):
            # Filling the initial graph entry in matrix
            if WMat[i,j,0] == 1:
                SP[i,j,0] = WMat[i,j,1]
            else:
                SP[i,j,0] = float('inf')
    
    
    # Repeat the process n times where n is number of vertices
    for k in range(1, cols+1):
        for i in range(rows):
            for j in range(cols):
                # Checking The shortest path distance for each pair in matrix 
                SP[i,j,k] = min(SP[i,j, k-1], SP[i, k-1, k-1] + SP[k-1, j, k-1])

    # Return the last updated matrix
    return SP[:,:,cols]
    # return SP
    


edges = [(0,1,10),(0,7,8),(1,5,2),(2,1,1),(2,3,1),(3,4,3),(4,5,-1),(5,2,-2),(6,1,-4),(6,5,-1),(7,6,1)]
size = 8
import numpy as np
W = np.zeros(shape=(size,size,2))
for (i,j,w) in edges:
    W[i,j,0] = 1
    W[i,j,1] = w    
print(floydWarshall(W))