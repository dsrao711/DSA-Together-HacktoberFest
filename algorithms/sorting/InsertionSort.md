### Insertion Sort

Consider an array a 
Steps : 
- Split the array into 2 halves : sorted and unsorted 
    - First half is sorted and consisting of a[0] (Left half)
    - Rest half is unsorted (Right Half)

    [![1.png](https://i.postimg.cc/63cV26BM/1.png)](https://postimg.cc/JDyHSLDX)

- Initialize the last index of  sorted arr with j (Since in the first iteration , sorted half consists of only 1 element i.e the first element j = 0) and first element of unsorted arr as i
    -> j = i-1

- Store a[i] in temp 

    [![3.png](https://i.postimg.cc/Zqh6wvRf/3.png)](https://postimg.cc/JsPynnjJ)

- Every element from the unsorted part has to be inserted in the sorted part .Compare temp with every element in the sorted part and store it its right position 
    - IF temp is smaller than a[j] , store a[j] in a[j+1] and keep checking in the sorted half till temp is  greater than a[j] by decrementing j and going to the left 

    [![4.png](https://i.postimg.cc/BQ6pFFLH/4.png)](https://postimg.cc/F1M057xH)
    
    [![2.png](https://i.postimg.cc/ZKGNqvrT/2.png)](https://postimg.cc/LnV5CXC7)

    - IF temp is greater than a[j] then it should 



