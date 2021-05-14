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
