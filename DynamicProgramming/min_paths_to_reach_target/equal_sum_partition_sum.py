
class Solution:
    def isSubsetSum(self,n, arr, sum):
        # code here 
        dp = ([[False for i in range(sum + 1)] 
            for i in range(n + 1)])
        
        for i in range(n + 1):
            dp[i][0] = True
        
        for i in range(1, n + 1):
            for j in range(1, sum + 1):
                if j<arr[i-1]:
                    dp[i][j] = dp[i-1][j]
                if j>= arr[i-1]:
                    dp[i][j] = (dp[i-1][j] or 
                                    dp[i - 1][j-arr[i-1]])
    
        return dp[n][sum]
        
    def equalPartition(self, N, arr):
        # code here
        arr_sum = sum(arr)
        # If sum is even , partition into equal halves is possible
        if(arr_sum % 2 != 0):
            return False
        # Check if equal half i.e 22/2 = 11 sum subset is present or not
        elif(arr_sum % 2 == 0):
            return self.isSubsetSum(N , arr , arr_sum//2)

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
