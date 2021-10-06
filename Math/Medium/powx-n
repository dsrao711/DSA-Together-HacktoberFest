class Solution:
    def myPow(self,x, n) :
        ans = 1.0
        if n<0 :
            n = n*(-1)
            while n>0:
                if n&1 :
                    ans = ans/x
                n>>=1
                x*=x
            return ans
            
        
        while n>0:
            if n&1 :
                ans = ans*x
            n>>=1
            x*=x
        return ans    
            
                
        
