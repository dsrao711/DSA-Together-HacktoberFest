# Approach:
# Just like Buy And Sell Stock 1, but here we have to keep track of consecutive peaks and valleys. 
# If the price for a day is greater than previous day, we count it as a transaction and add the profit.

def maxProfit(prices):
    min_so_far = prices[0]
    max_profit = 0
    n = len(prices)
    for i in range(1, n) :
        if(prices[i] > prices[i-1]) :
            max_profit += (prices[i] - prices[i-1])
        
    return max_profit

arr = []
n = int(input("Enter the number of elements in the array : "))

for i in range(0, n):
    element = int(input())
    arr.append(element) 

output = maxProfit(arr)
print(output)