for i in range( 1, len(arr) ):

            if oneDel == float( '-inf' ):
                v1 = arr[i]
            else:
                v1 = oneDel + arr[i]
            
            oneDel = max ( v1, noDel )

            noDel = max ( noDel + arr[i], arr[i] )

            res = max ( res, oneDel, noDel )
        
        return res