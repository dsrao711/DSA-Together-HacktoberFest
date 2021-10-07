
class Solution:
    def isPlaindrome(self, S):
        # code here
        reverse = S[::-1]
        if (S == reverse):
            op = 1
        else:
            op = 0
        return op

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.isPlaindrome(S)
        print(answer)

# } Driver Code Ends