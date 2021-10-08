#Link to the problem: https://practice.geeksforgeeks.org/problems/find-position-of-set-bit3706/1

#Code:

class Solution:
    def findPosition(self, N):
        if(N == 0):
            return -1
        if(N & (N - 1) == 0):   #checking for power of two
            i = 1               #if it's a power of two then it will have only one
            cnt = 0             #set bit, otherwise it will have more than one set bit
            while(N > 0):
                N = N>>i  
                cnt += 1
            return cnt
        else:                   #hence, returning -1
            return -1

if __name__ == '__main__': 
    t = int (input ("Enter number of Test cases: "))
    for _ in range (t):
        N = int(input("Enter number: "))
        
        ob = Solution()
        print("Position of set-bit: ", ob.findPosition(N))

#Time Complexity: O(log(N))
#Space Complexity: O(1)
