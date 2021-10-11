
def maxProfit(prices):
    transaction1 = float('inf')
    transaction2 = float('inf')
    profit1 = 0
    profit2 = 0

    for i in prices :
        transaction1 = min(transaction1, i)
        profit1 = max(profit1, (i - transaction1))
        
        transaction2 = min(transaction2, (i - profit1))
        profit2 = max(profit2, (i - transaction2))
      
    return profit2

arr = []
n = int(input("Enter the number of elements in the array : "))

for i in range(0, n):
    element = int(input())
    arr.append(element) 

output = maxProfit(arr)
print(output)