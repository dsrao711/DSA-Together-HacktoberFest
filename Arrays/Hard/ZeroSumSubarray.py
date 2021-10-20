"""Here return the subarray having the Sum = 0
The Code wants us to solve the problem without using the conventional technique of two for loops!

NOTE:- The complexity must be O(n)"""

# Problem statement Link --> https://practice.geeksforgeeks.org/problems/zero-sum-subarrays1825/1

# from time import time

data = list(map(int, input().split()))  # 4 1 -1 2 -1 3
# start = time()                                      
new = []
seen = set()
i = 0
for a in data:
    if len(new) == 0:
        new.append(a)
        seen.add(a)
    else:
        new.append(new[i] + a)
        if (new[i] + a) not in seen:
            seen.add(new[i] + a)    #if not in the seen set, add the element with the ith element present in the new[i]
        else:
            print(f"{new.index(new[i] +a) +1} -->  {i +1}")     #Finally prints the Index Sequence of the Contiguous subarray whose sum is 0
            break
        print(seen)
        i += 1
# print(time() - start)
print(new)
