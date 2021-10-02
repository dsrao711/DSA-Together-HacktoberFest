#https://practice.geeksforgeeks.org/problems/find-pair-given-difference1559/1#

# Approach : 

# Using Two Pointer techq
# Sort the array before applying two pointer approach
class Solution:

    def findPair(self, arr, L,N):
        
        arr.sort()
        i,j = 0,1
        flag = 0
        size = len(arr)
        while( i < size and j < size):
            
            if(i != j and arr[j]-arr[i] == N):
                flag = 1
                break
            
            elif(arr[j] - arr[i] < N):
                j +=1
            else:
                i +=1
                
        if(flag == 1):
            return True
        else:
            return False
            
               

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        L,N = [int(x) for x in input().split()]
        arr = [int(x) for x in input().split()]

        solObj = Solution()

        if(solObj.findPair(arr,L, N)):
            print(1)
        else:
            print(-1)
# } Driver Code Ends