# Selection Sort :

<hr>

[![1.png](https://i.postimg.cc/mg34KhRX/1.png)](https://postimg.cc/VJN2CfJn)

Consider an array a = [2,4,8,9,5]

Similar to Insertion Sort , Divide the array to 2 halves : Sorted and Unsorted 

Approach :

- Assign minimum element = a[0]
- Find the smallest element from the unsorted array and swap it with the ith element in the sorted array 

Steps :

1. Divide the array into 2 halves
2. index for sorted half : i , index for unsorted half = j -> j = i+1
3. Assign minimum = a[i]
4. Iterate through unsorted half and find an element smaller than a[i] , if found -> store the new minimum in minimum 
5. Swap minimum with a[i]

[![2.png](https://i.postimg.cc/ydPcbZyy/2.png)](https://postimg.cc/ygDDJW5D)
