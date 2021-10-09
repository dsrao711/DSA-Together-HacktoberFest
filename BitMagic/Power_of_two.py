#Link to the problem: https://practice.geeksforgeeks.org/problems/power-of-2-1587115620/1


#Code:

class Solution:
    def isPowerofTwo(self,n):
        if n == 0:
            return 0
        if (n & (n-1) == 0):   #if a number is power of 2, then its AND with
            return 1           #(number-1) will be 0, hence returning 1
        else:
            return 0           #otherwise returning 0

import math

def main():
    
    T = int(input("Enter test cases: "))
    
    while(T > 0):
        n = int(input("Enter number: "))
        ob = Solution()
        if ob.isPowerofTwo(n):
            print("YES")
        else:
            print("NO")
        
        T -= 1

if __name__=="__main__":
    main()

#Time Complexity: O(log(N))
#Space Complexity: O(1)
