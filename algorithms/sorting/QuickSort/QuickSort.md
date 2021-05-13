# Quick Sort

- Uses Divide and Conquer

## Steps :

[![1.jpg](https://i.postimg.cc/44HknsFf/1.jpg)](https://postimg.cc/G9RS5wCV)


<u>Partition:</u>

1. Increment i until an element greater than pivot is found
2. Decrement j until and element lesser than pivot is not found
3. Once found , swap these two elements
4. Once j is greater than i , swap j with pivot

<u>Quick Sort:</u>

- Get the Pivot element's position from Partition process and apply Quick sort on both left and right side of the pivot 


<b>Partition Process </b>

```
Partition(l, h):
    pivot = a[l]
    i = l
    j = h
    while(i < j):
        while(a[i] < pivot):
            i++
        while(a[j] > pivot):
            j--
        if(i < j ):
            swap a[i] and a[j]
    swap a[j] with pivot
    
    return j #sorted position of  pivot element
```

<b>Quick sort</b>

```
if(l<h):
    pivot = Partition(l , h)
    QuickSort(l , pivot-1)
    QuickSort(pivot+1 , h)


```
