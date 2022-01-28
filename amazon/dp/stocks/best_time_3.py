# Problem : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/submissions/
# Ref : https://youtu.be/wuzTpONbd-0

# 2 transactions only 
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        
        # Calc dp - left  -> Max profit so far - Buy before and sell today / before 
        # Similar to one transaction buy sell stock problem 
        
        max_profit_till_today = 0
        min_so_far = prices[0]
        dp_left = [0]*n
        
        for i in range(1 , n):
            # Calculate best buying day -> min before the current selling day
            min_so_far = min(min_so_far , prices[i])
            # Calc profit for current day
            max_profit_till_today = prices[i] - min_so_far
            # Update the global max profit possible uptil today
            dp_left[i] = max(dp_left[i-1] , max_profit_till_today )
        print(dp_left)
        # Cal dp - right  -> Max profit so far - Buy today/later and sell later 
        
        max_profit_from_today = 0
        max_from_today = prices[n-1]
        dp_right = [0]*n
        
        for i in range(n-2 , -1 , -1 ):
            # Calculate best selling day -> max from today - current buying day
            max_from_today = max(max_from_today , prices[i])
            # Calc profit for today
            max_profit_from_today = max_from_today - prices[i]
            # Update the global profit possible from today 
            dp_right[i] = max(dp_right[i+1] , max_profit_from_today)
            
        # Calc max( dp-right + dp-left )
        
        max_profit = 0 
        
        for i in range(0 , n):
            sum_of_2 = dp_right[i] + dp_left[i]
            max_profit = max(sum_of_2 , max_profit)
            
        return max_profit