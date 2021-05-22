[![Screenshot-2021-05-20-221424.png](https://i.postimg.cc/BnvNJ6dy/Screenshot-2021-05-20-221424.png)](https://postimg.cc/7fpSVxPM)

Using Two Pointer method : 
- Sort the array to perform 2 pointer
- Initialize two pointers i and j at 0th and 1st index
- Apply the two pointer method for the array from (j+1)th index
- Find the indexes whose sum and sum of ith and jth index = Target such that we find the quadraplet 

- Since we need unique charachters in every subarray , we need to check if there are duplicates 

#### Condition for duplicates : 
- The next/previous element should not be equal for current element 