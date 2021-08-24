# KnapSack Problem :

[![22.png](https://i.postimg.cc/CKh27SKY/22.png)](https://postimg.cc/pmSkXN81)

Consider a bag of capacity = m (Knapsack capacity)

Consider objects O , with Profits P and weight W

We need to fill the container with objects and the sum of all these weights should be less than equal to m

If we fill the more objects with less weight , we can fill more number of objects but here we would be ignoring the 
profit factor .

So , we can consider the profit by weight ratio 

p/w ratio would be max when either Profit is high or Weight is low which satisfies both the factors 

Hence we will keep filling the objects in order of P/W ratio until we reach the knapsack capacity

Input includes : Weight , Profit of Objects and KnapSack capacity

Output : Total Profit(T) after filling the objects in the bag

### Steps : 

- Sort the objects according the p/w ratio

- Iterate through the objects and check if the Capacity - weight >= 0 , since the sum of all weights should not exceed the capacity

- If the Capacity - weight >= 0  , Subtract the weight from capacaity and add the profit value Total Profit (T)

- Else , If the capacity - weight < 0 i.e the limit for capacity left is suppose 2 kg and we have the value left as 3 kg , then we will be considering the fraction 2/3 and adding the 2/3 profit of that object to the total Profit


### Algorithm:
```

capacity = 50
weights = [10,20,30] 
profits = [60,100,120]

objects = []
tot_profit = 0

for i in range(5):
    objects.append((weight[i],profit[i],capacity))

objects.sort()

for i in objects :
    obj_weight = i.weight
    obj_profit = i.profit 

    if(capacity - obj.weight >= 0):
        # Subtract the weight from capacity and add the profit to total profit

        capacity -= obj.weight
        tot_profit += obj.profit
    
    else:
        #Subtract the fraction i.e curr.weight/capacity from the capacity and add the fraction*profit into total profit

        fraction = obj.weight/capacity
        capacity = capacity - fraction*obj.weight
        tot_profit = tot_profit + fraction*obj.profit


return tot_profit

```