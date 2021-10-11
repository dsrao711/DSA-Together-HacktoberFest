
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