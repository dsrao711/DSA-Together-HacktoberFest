#https://practice.geeksforgeeks.org/problems/swap-two-nibbles-in-a-byte0446/1/?company[]=Accolite&company[]=BrowserStack&company[]=Accolite&company[]=BrowserStack&page=1&query=company[]Accolitecompany[]BrowserStackpage1company[]Accolitecompany[]BrowserStack#

class Solution:
    def swapNibbles (self, x):
        # code here 
        return ( (x & 0x0F)<<4 | (x & 0xF0)>>4 )

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.swapNibbles(N))
# } Driver Code Ends