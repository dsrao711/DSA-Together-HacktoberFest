```

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

```

## Steps : 

1. Create a list *merged* to store the merged intervals
2. Condition for merging  : If the first index of current interval is less than last index of previous interval 
3. If condition satisfies , replace the last index of previous interval with the maximum between current and previous interval's last index
4. If not , then simply append the interval in the merged list 