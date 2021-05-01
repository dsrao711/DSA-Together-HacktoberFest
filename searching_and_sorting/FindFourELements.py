from itertools import combinations
from collections import defaultdict

def fourSum(arr, k):
        # code here
    arr.sort()
    combs = []
    op = defaultdict()
    combs = list(combinations(arr , 4))
    
    for comb in combs :
        
        if (sum(comb) == k):
            comb_str = ' '.join([str(elem) for elem in comb])
            if not comb_str in op:
                op[comb_str] = True
            
    print(list(op.keys()))
    res = []
    result = []
    for i in op.keys():
        
        a = list(map(int,i.split(' ')))
        for j in a :
            res.append(j)
        result.append(res)
        
    return result
 
                
    
   
        
        
      
    

b = [1,2,3,4,5,6,7,11]
fourSum(b, 10)
