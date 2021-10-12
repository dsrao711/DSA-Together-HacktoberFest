#https://leetcode.com/problems/find-missing-observations
class Solution:
    def missingRolls(self, rolls, mean, n):
        m = len(rolls)
        ans =[]
        tot = mean*(n+m) # total sum of rolls
        sm = 0 
        for i in range(m):
            sm+=rolls[i]   # sum of m observation
        tot-=sm            # sum of remaining n observation
        if tot<n or tot>6*n:
            return ans      # return empty if sum is not possible    
        

        av = tot//n         # calculating average to assign each entry with it
        for i in range(n):
            ans.append(max(av,1))
            tot-=max(av,1)  
        i = 0  
        # now we are trying to increase every entry greedly until we hit the total sum
        while tot>0:    
            val =(min(6-ans[i],tot))
            tot-=val
            ans[i] +=val
            i+=1
        return ans
# Time Complexity: O(n)
      
