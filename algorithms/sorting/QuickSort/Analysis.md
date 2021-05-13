# Analysis of Quick sort algorithm :

## Best Case :

Consider a list ,
```
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
```

[![3.png](https://i.postimg.cc/WbsnC7ZB/3.png)](https://postimg.cc/c65w8wXh)
[![2.jpg](https://i.postimg.cc/FzNyt9Yy/2.jpg)](https://postimg.cc/KkpkBhrj)

If the pivot element is median of the aaray i.e if partioning is happening at the center

### Time Complexity : O(nlogn)
<hr>

## Worst case : 

Consider a list,

    a = [2,4,8,10,16,18,17]

[![3.jpg](https://i.postimg.cc/bNFtg09H/3.jpg)](https://postimg.cc/4mVyN9Mm)

Time Complexity : O(n^2)

If the list is already sorted , Then worst case can occur

## For improving the performance :

1 . Select middle element as Pivot 
2 . Select random element as Pivot 


## Space Complexity 

Can vary from O(logn) to O(n)