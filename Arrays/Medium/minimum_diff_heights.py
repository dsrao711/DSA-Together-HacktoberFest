# 

class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        # Sort
        arr.sort()
        curr_min = arr[0]
        curr_max = arr[n-1]
        res = curr_max - curr_min
        for i in range(1,  n):
            curr_min = min(arr[0] + k , arr[i]-k)
            curr_max = max(arr[n-1] - k , arr[i-1] + k)
            if(curr_min >= 0):
                res = min(res , curr_max - curr_min)
        
        return res
 
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1
