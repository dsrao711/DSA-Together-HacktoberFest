class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        max_profit = 0
        n = len(prices)
        for i in prices :
          min_so_far = min(min_so_far , i)
          profit = i - min_so_far
          max_profit = max(max_profit , profit)
        return max_profit
