class Solution():
    def sort012(self,arr,n):
        # code here
        cnt_1 = 0
        cnt_2 = 0 
        cnt_0 = 0
        for i in range(0 , n):
            if(arr[i] == 0):
                cnt_0 += 1
            elif(arr[i] == 1):
                cnt_1 += 1
            else: 
                cnt_2 += 1
        
        i = 0
        
        while(cnt_0 > 0):
            arr[i] = 0
            i += 1
            cnt_0 -= 1
            
        while(cnt_1 > 0):
            arr[i] = 1
            i += 1
            cnt_1 -= 1
        
        while(cnt_2 > 0):
            arr[i] = 2
            i += 1
            cnt_2 -= 1
        
        return arr


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends