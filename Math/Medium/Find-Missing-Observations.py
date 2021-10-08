#https://leetcode.com/problems/find-missing-observations
class Solution:
    def missingRolls(self, rolls, mean, n):
        m = len(rolls)
        ans =[]
        tot = mean*(n+m)
        sm = 0 
        for i in range(m):
            sm+=rolls[i]
        tot-=sm
        if tot<n or tot>6*n:
            return ans
        
        av = tot//n
        for i in range(n):
            ans.append(max(av,1))
            tot-=max(av,1)
        i = 0  
        while tot>0:
            val =(min(6-ans[i],tot))
            tot-=val
            ans[i] +=val
            i+=1
        return ans
# Time Complexity: O(n)
      
