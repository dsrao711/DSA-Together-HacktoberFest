# https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/submissions/

# Approach1 - 
# We need to return the minimum cost required to delete the duplicates in a list
# We need to delete those duplicates with minimum cost 

# Variables :
#prev_index = 0
# i = 1
# total_cost = 0
# We iterate through the string  to check duplicates , if a duplicate is found i.e
# If s[i] == s[prev_index] --> total_cost += min(s[i] , s[prev_index]) , shift the prev_index to i
# Else : Update the prev_index to i 
# Return total_cost
class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        total_cost = 0
        prev_index = 0
        i = 1
        n = len(s)
        while(i < n):
          if(s[prev_index] == s[i]):
            total_cost += min(cost[prev_index] , cost[i])
            if(cost[prev_index] < cost[i]):
              prev_index = i
          else:
            prev_index = i
          
          i += 1
          
        return total_cost