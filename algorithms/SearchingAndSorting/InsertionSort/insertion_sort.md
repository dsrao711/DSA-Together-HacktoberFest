### Insertion Sort

Consider an array a = [8,4,9,2]
Steps : 
- Split the array into 2 halves : sorted and unsorted 
    - First half is sorted and consisting of a[0] (Left half)
    - Rest half is unsorted (Right Half)

    [![1.png](https://i.postimg.cc/XqwgjKpy/1.png)](https://postimg.cc/JHzXKk31)

- Initialize the last index of  sorted arr with j (Since in the first iteration , sorted half consists of only 1 element i.e the first element j = 0) and first element of unsorted arr as i
    -> j = i-1

- Store a[i] in temp 

    [![3.png](https://i.postimg.cc/Zqh6wvRf/3.png)](https://postimg.cc/JsPynnjJ)

- Every element from the unsorted part has to be inserted in the sorted part .Compare temp with every element in the sorted part and store it its right position 
    - IF temp is smaller than a[j] , store a[j] in a[j+1] and keep checking in the sorted half till temp is  greater than a[j] by decrementing j and going to the left 

        [![4.png](https://i.postimg.cc/BQ6pFFLH/4.png)](https://postimg.cc/F1M057xH)

        [![2.png](https://i.postimg.cc/ZKGNqvrT/2.png)](https://postimg.cc/LnV5CXC7)

    - IF temp is greater than a[j] then it should be at the last position of the sorted half. Hence , store the temp value at the last postition i.e j+1
        a[j+1] = temp

        [![5.png](https://i.postimg.cc/BZ8kWRpd/5.png)](https://postimg.cc/jCbZPgGX)

##### Last iteration

[![6.png](https://i.postimg.cc/pTvrNDbS/6.png)](https://postimg.cc/4K8sVH3v)

[![7.png](https://i.postimg.cc/mDdsdMbC/7.png)](https://postimg.cc/dkTp3hZV)

[![8.png](https://i.postimg.cc/HLzDx58R/8.png)](https://postimg.cc/hJX3ZXr1)

[![9.png](https://i.postimg.cc/QMNsps5F/9.png)](https://postimg.cc/DSNtT9xh)

[![10.png](https://i.postimg.cc/DzzkS6ks/10.png)](https://postimg.cc/pm317DdX)


