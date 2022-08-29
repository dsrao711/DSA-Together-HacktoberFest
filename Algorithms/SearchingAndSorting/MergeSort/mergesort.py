def mergesort(arr):
    
    if len(arr) <= 1:
        return
    
    n = len(arr)
    mid = len(arr) // 2
    l = arr[0]
    h = arr[n-1]
    
    mergesort(l , mid)
    mergesort(mid+1 , h)

    op = merge_sorted_list(l , h , arr)
    return op

def merge_sorted_list(a, b, arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0
    
    while (i < len_a and j < len_b):
        
        if(a[i] <= b[j]):
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1
        
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        arr[j] = b[j]
        j += 1
        k += 1
        
    return arr


if __name__ == '__main__':

    op = mergesort([34,11,4,5,6,67,67,8,])
    print(op)
    