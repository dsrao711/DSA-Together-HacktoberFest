
def sumElement(arr,n):
    #code here
    def sum (arr) :
        total = 0
        for i in range (0 ,n):
            total = total + arr[i]
        return total
    
    return(sum(arr))

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    testCase=int(input())
    
    for _ in range(testCase):
        n=int(input())
        arr=[int(x) for x in input().split()]
        
        print(sumElement(arr,n))
# } Driver Code Ends