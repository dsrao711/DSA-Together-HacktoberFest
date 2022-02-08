# https://leetcode.com/problems/gas-station/
# 


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
        n = len(gas)
        # Condition 1 - gas_sum == cost_sun
        if(sum(gas) < sum(cost)):
            return -1
        # starting index to complete the cycle -> op
        start = 0 
        # Difference between gas and cost for travelling per station 
        total = 0 
        
        for i in range(n):
            total += gas[i] - cost[i]
            # Condition 2 - Difference cannot be negative
            if(total < 0 ):
                # Condition 3 - Since only unique soln exists , the first index found 
                # which has difference greater than 0 and since condition 1 and 2 are already satisfied , start is the final answer
                start = i + 1
                total = 0
                
        return start