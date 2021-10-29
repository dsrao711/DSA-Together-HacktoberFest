from functools import lru_cache

@lru_cache(maxsize = 1000)
class Solution:
    def tribonnaci(self, n:int):
        assert n>=0, "You must pass a non-negative integer"
        return self.aux_tribonnaci(n)

    def aux_tribonnaci(self, n:int, t_0=0, t_1=1,t_2=1):
        if n==0:
            return t_0
        else:
            return self.aux_tribonnaci(n-1, t_0=t_1, t_1=t_2, t_2=t_2+t_1+t_0)