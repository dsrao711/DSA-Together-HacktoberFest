def maxSubArraySum(a,size):
   
   max_current = a[0]
   max_global = max_current
   for i in range (1 , size):
       max_current = max(max_current + a[i] , a[i])
       max_global = max(max_current , max_global)
   return max_global
    
