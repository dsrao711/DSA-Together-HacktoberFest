# question : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/
# ref : https://youtu.be/HWJ9kIPpzXs

# Infinite transactions 
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        bd = 0 
        sd = 0
        profit = 0 
        
        for i in range (1 , len(prices)):
            # Check for highs 
            if(prices[i] > prices[i-1]):
                sd += 1 
            else:
                # Dip found
                # Calc the previous profit
                profit += prices[sd] - prices[bd]
                # Reinitialize new buying and selling day 
                bd = i 
                sd = i
                
        # If a stroke is found but the loop ends, calculate the remaining stroke
        profit += prices[sd] - prices[bd]
        
        return profit
        