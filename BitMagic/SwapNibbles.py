#https://practice.geeksforgeeks.org/problems/swap-two-nibbles-in-a-byte0446/1/?company[]=Accolite&company[]=BrowserStack&company[]=Accolite&company[]=BrowserStack&page=1&query=company[]Accolitecompany[]BrowserStackpage1company[]Accolitecompany[]BrowserStack#

# #100 in binary is 01100100,  two nibbles are (0110) and (0100) If we swap the two nibbles, we get 01000110 which is 70 in decimal
class Solution:
    def swapNibbles (self, x):
        # 0x0f -> 0000 1111 
        # x& 0x0F gives the last four digits of the number nd x & 0xF0 gives the first four digits of the number
        # Shifting four positions to the left of the last 4 digits and shifting first four digits to the right gives us the swapped nibbles 
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