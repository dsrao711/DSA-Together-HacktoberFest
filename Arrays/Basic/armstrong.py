class Solution:
    def armstrongNumber (ob, n):
        # code here 
        number = str(n)
        arm = 0
        for i in range(0 , len(number)):
            arm += pow(int(number[i]) , len(number))
        if(arm == n):
            return "Yes"
        else:
            return "No"
            
          
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends
