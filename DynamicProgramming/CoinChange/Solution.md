#### In the given problem , we are supposed to find minimum number of coins to get the sum equal to the amount given

#### For given example
- Input :

1. coins = [7 , 5 , 1]
2. amount = 18

- O/p :
    4

We can achieve 18 by 
- 2 Coins of 5
- 1 coin of 7
- 1 coin of 1
- Sum = 4

18 can be achieved by various combinations of 7 , 5 , 1

[![cc.png](https://i.postimg.cc/282dbKPx/cc.png)](https://postimg.cc/4mHHjB4K)

Lets call 11 , 13 , 17 , 6 , 12 , 10 ... as subSums

As shown above , 6 has been calculated previously and later on 6 is required in latter part .
Instead of computing it again , we can store the value for 6 i.e 2 (1 coin of 5 and 1 coin of 1)

As we need to store the value of recursion ie. Subsums in a memory , hence we choose DP here

Consider a list rs = [] with size equal to the amount

rs[] stores the number of coins required for each number from  1, 2 ,...amount 
We are supposed to return rs[amount] 

In this case rs[18] returns the minimum coins required to produce the sum 18

