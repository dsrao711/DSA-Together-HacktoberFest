class Solution:
    def perfectSum(self, a, n, sum):
        # code here  
        dp = [[0] * (sum + 1) for i in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, sum + 1):
            dp[0][i] = 0
        # mod 10^7 since ans can be large - given in prob statement
        for i in range(1, n+1):
            for j in range(sum + 1):
                if a[i-1] <= j:
                    dp[i][j] = (dp[i-1][j] + dp[i-1][j-a[i-1]]) %1000000007
                else:
                    dp[i][j] = (dp[i-1][j]) % 1000000007
                    
        return (dp[n][sum]) %1000000007 



if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n,sum = input().split()
        n,sum = int(n),int(sum)
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.perfectSum(arr,n,sum)
        print(ans)

