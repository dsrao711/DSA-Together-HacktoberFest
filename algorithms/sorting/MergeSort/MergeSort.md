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


Time Complexity : 

- T(n/2) + T(n/2) + n for n >1
- 1 for n = 1

[![14.png](https://i.postimg.cc/bNSCMLWW/14.png)](https://postimg.cc/tYyNndXN)