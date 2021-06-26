# 1 . Tabulation - Bottom Up approach (Iterative)

def fib_bottom_up(n):
    
    if n == 1 or n == 2:
        return 1
    
    bottom_up = [None] * (n+1)
    
    bottom_up[1] = 1
    bottom_up[2] = 1
    
    for i in range(3, n+1):
        
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
        
    return bottom_up[n]




# 2 . A memoized solution - Top down approach

def fib_2(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_2(n-1, memo) + fib_2(n-2, memo)
    memo[n] = result
    return result

def fib_memo(n):
    memo = [None] * (n + 1)
    return fib_2(n, memo)


output = fib_memo(123456789)

print(output)


# 3. Memoization using caching
# To memoize a function in Python, we can use a utility supplied in Python’s standard library—the functools.lru_cache decorator.

# https://leetcode.com/problems/fibonacci-number/submissions/


from functools import lru_cache

@lru_cache(maxsize = 1000)
class Solution:
    def fib(self, n: int) -> int:
        if(n==0):
          return 0
        if(n==1 or n == 2):
          return 1
        elif(n>2):
          return self.fib(n-1) + self.fib(n-2)
      
      
      
#lru_cache - https://www.infoworld.com/article/3606188/speed-up-python-functions-with-memoization-and-lrucache.html