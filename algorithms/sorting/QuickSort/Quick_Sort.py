def QuickSort(l):
    if(len(l)<=1):
        return l
    return (QuickSort([i for i in l[1:] if i<l[0]]) + ([i for i in l if i==l[0]]) + QuickSort([i for i in l[1:] if i>l[0]]))
l=[1,4,3,5,7,4,5,3,7,1,5,8,3,6]
print(QuickSort(l))