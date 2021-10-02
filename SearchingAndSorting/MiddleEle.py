
class Solution:
    def middle(self,A,B,C):
        #code here
        if((A>B and A<C) or (A>C and A<B)):
            return A
        if((B>A and B<C) or (B>C and B<A)):
            return B
        else:
            return C

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        A,B,C=map(int,input().strip().split())
        ob=Solution()
        print(ob.middle(A,B,C))
# } Driver Code Ends