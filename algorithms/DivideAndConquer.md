
# Divide and Conquer

<hr>

- Problem should be same as subproblem 
- recursive

### Algorithm:

 [![Cam-Scanner-05-14-2021-00-07-1.jpg](https://i.postimg.cc/6Qn9V7sW/Cam-Scanner-05-14-2021-00-07-1.jpg)](https://postimg.cc/PLfsT5r9)

 ```

 P:Problem
 S: Solution

DAC(P)
    if(small(P)):
        S(P)
        
    else:
        Divide P into P1 , P2 , P3 , ... PK
        Apply DAC(P1) , DAC(P2)
        Combine (DAC(P1) , DAC(P2) , DAC(P3)...)

```

### Applications of DAC

1. Binary Search
2. Finding max and min
3. Merge Sort
4. Quick Sort
5. Strassen's Matrix Multiplication
