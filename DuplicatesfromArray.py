
class Solution:    
    def remove_duplicate(self, A, N):
#         # code here
#         output = list(dict.fromkeys(A))
#         return len(output)
        
        if (N == 0 or N == 1):
            return N
        
        temp = list(range(N))
        j = 0 
      
        for i in range(0 ,N-1):
            if(A[i] != A[i+1]):
                temp[j] = A[i]
                j += 1
        temp[j] = A[N-1]
        j += 1

        for i in range(0 , j):
            A[i] = temp[i]
        return j
#{ 
#  Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        n = ob.remove_duplicate(A,N)
        for i in range(n):
            print(A[i], end=" ")
        print()


# } Driver Code Ends