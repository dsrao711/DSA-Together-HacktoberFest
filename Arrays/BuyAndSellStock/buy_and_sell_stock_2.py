
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