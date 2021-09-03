# https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/submissions/

# Approach2:

# s = "aaabbabbbb"
# cost = [3, 5, 10, 12, 10 , 2 , ,3 , 2 , 3 , 4]
# Here we calculate the local max and local sum of all the duplicates 
# So for "aaa" -> Local sum = 3+5+10 = 18 , Local sum = 10 
# So since we need to take out the letters which cost minimum amount , we keep the letter with max amount
# And remove the rest
# So the formula is : Amount = Local sum - Local max

# We keep on checking for set of duplicates , apply the above formula and keep adding the amount to final answer

# Variables : 
# s_sum = 0 (Local sum)
# s_max = 0 (Local max)
# ans  (Total amount to delete the letters)


class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        n = len(s)
        s_sum = 0   
        s_max = 0
        ans = 0
        
        for i in range(0 , n):
        # Check when substring of duplicates end 
          if(s[i] != s[i-1] and i > 0):
            # add the amount in final ans 
            ans += s_sum - s_max
            # Reset these variables 
            s_sum = 0
            s_max = 0
            
          s_sum += cost[i]
          s_max = max(s_max , cost[i])

        # For corner case - "bbbb" in the example string considered above , we need to add the amount of
        # last duplicated in the op if there are any 
        ans += s_sum - s_max
        
        return ans