#

# Approach 1

class Solution:
    def setBits(self, n):
        # Keep counting until n is 1 
        count = 0
        while(n):
            count += n&1
            n >>= 1
            
        return count

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        ob = Solution()
        ans = ob.setBits(N)
        print(ans)




# } Driver Code Ends



# Approach 2 - Use python inbuilt bin() function


class Solution:
    def setBits(self, n):
        # code here
        return bin(N).count('1')

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        ob = Solution()
        ans = ob.setBits(N)
        print(ans)




# } Driver Code Ends


