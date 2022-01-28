# 1 Transaction only 
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        # Buying day 
        min_so_far = prices[0]
        n = len(prices)
        
        for i in range(0 , n):
            # Find the lowest buying day 
            min_so_far = min(prices[i] , min_so_far)
            # Calculate profit for today
            profit_if_sold_today = prices[i] - min_so_far 
            # Update max profit
            max_profit = max(profit_if_sold_today , max_profit)
            
        return max_profit
        
        
    