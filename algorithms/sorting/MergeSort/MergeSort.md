# Merge Sort

- Uses Divide and Conquer 
- Recursive

### Algorithm :


Merge sort divides the list into equal halves recursively and sorts each half to return the sorted list 

Consider a list A ,

[![11.png](https://i.postimg.cc/tgcs74TD/11.png)](https://postimg.cc/v1WYNM56)

*Merge Sort*

```
MergeSort(l,h):
    if(l<h):
        mid = (l+h)/2           #1
        MergeSort(l,mid)        # T(n/2)
        MergeSort(mid+1,h)      # T(n/2)
        Merge(l,mid,h)          # n

```
[![msort.png](https://i.postimg.cc/MKtx44Lb/msort.png)](https://postimg.cc/N5yW2NB5)

[![time.jpg](https://i.postimg.cc/Ss1tMPYQ/time.jpg)](https://postimg.cc/MMRDkdYg)


## Merge Sort Time and Space Complexity

1. Space Complexity
Auxiliary Space: O(n)

Sorting In Place: No

Algorithm : Divide and Conquer


2. Time Complexity
- Merge Sort is a recursive algorithm and time complexity can be expressed as following recurrence relation.

- T(n) = 2T(n/2) + O(n)             i.e (T(n/2) + T(n/2) + n )


- The solution of the above recurrence is O(nLogn). The list of size N is divided into a max of Logn parts, and the merging of all sublists into a single list takes O(N) time, the worst-case run time of this algorithm is O(nLogn)
```
- Best Case Time Complexity: O(n*log n)

- Worst Case Time Complexity: O(n*log n)

- Average Time Complexity: O(n*log n)

```

- The time complexity of MergeSort is O(n*Log n) in all the 3 cases (worst, average and best) as the mergesort always divides the array into two halves and takes linear time to merge two halves.