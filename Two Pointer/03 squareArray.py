# 977. Squares of a Sorted Array

# **Difficulty:** Easy  
# **Tags:** Topics, Companies

# ## Description

# Given an integer array `nums` sorted in **non-decreasing** order, return *an array of **the squares of each number** sorted in non-decreasing order*.

# ---

# ## Examples

# ### Example 1:
# **Input:** `nums = [-4,-1,0,3,10]`  
# **Output:** `[0,1,9,16,100]`  
# **Explanation:** After squaring, the array becomes `[16,1,0,9,100]`.  
# After sorting, it becomes `[0,1,9,16,100]`.



class Solution:
    from typing import List
    
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        siz=len(nums)

        # separate both positive and negative array
        # for i in range(0,siz-1):
        #     if nums[i] >= 0:
        #         a.append(nums[i])
        #     else:
        #         b.append(nums[i])

        for num in nums:
            if num<0:
                b.append(num)
            else:
                a.append(num)
                
        
        # CASE 01 : if any one array turns to be empty
        if len(a)==0:
            sq= [x*x for x in b]
            sq.reverse()
            return sq    
        
        if len(b)==0:
            sq= [x*x for x in a]
            return sq
        
        # CASE 02 : if both array are present and exist
        a = [x*x for x in a]
        b = [x*x for x in b][::-1]
            #length of both positive and negative array
        n,m = len(a), len(b)
            #set a 2 pointer to zero
        i=j=0
        sortSq=[]

        while i<n and j<m:
            if a[i]<=b[j]:
                sortSq.append(a[i])
                i+=1
            else:
                sortSq.append(b[j])
                j+=1                
        
        while j<m:
            sortSq.append(b[j])
            j+=1
        while i<n:
            sortSq.append(a[i])
            i+=1

        return sortSq


array=Solution()
nums= [-5,-3,-2,-1]
print(array.sortedSquares(nums))
