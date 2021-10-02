# Link : https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/1

class Solution:
    
    def findTwoElement( self,arr, n): 
        # code here
        
        number_map = {}
        rep_ele = -1
        miss_ele = -1
        for i in arr:
            
            if not i in number_map:
                number_map[i] = True
            else:
                rep_ele = i
                
        for i in range(1 , n+1):
            if not i in number_map:
                miss_ele = i
                
        ans = [rep_ele , miss_ele]
        return ans
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends