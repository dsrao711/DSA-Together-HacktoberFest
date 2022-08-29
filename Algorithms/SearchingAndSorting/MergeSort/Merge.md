# Merge

[![15.png](https://i.postimg.cc/D0vWGCsZ/15.png)](https://postimg.cc/dkftPj5P)


## Algorithm :

```
Merge(A,B,m,n):

    i = j = k = 0

    # Comparing and Copying elements 

    while(i <= m and j <=n)
        if(A[i] < B[j]):
            C[k++] = A[i++]
        else:
            C[k++] = B[j++]

    # append the remaining elements from A and B 

    while (i < len(A)):
        C[k++] = A[i++]

    while (j < len(B)):
        C[k++] = B[j++]




```

