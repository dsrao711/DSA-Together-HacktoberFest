# Approach:
# We need to find the lowest point (valley) and the highest point (peak) such that peak is after valley.
# Finding the difference between them will give us the maximum profit.
# For this, we keep track of the lowest point (min_so_far) and the maximum profit (max_profit).

def maxProfit(prices):
    min_so_far = prices[0]
    max_profit = 0
    n = len(prices)
    for i in prices :
        min_so_far = min(min_so_far , i)
        profit = i - min_so_far
        max_profit = max(max_profit , profit)
      
    if(max_profit == 0):
        return -1
        
    return max_profit

arr = []
n = int(input("Enter the number of elements in the array : "))

for i in range(0, n):
    element = int(input())
    arr.append(element) 

output = maxProfit(arr)
print(output)