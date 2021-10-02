    
class Solution():

    def majorityElement(self, arr, n):
        #Your code here
        arr.sort()
        count = 1
        max_ele = -1
        temp = arr[0]
        flag = 0
        
        for i in range(1,n):
            
            if(temp == arr[i]):
                count += 1
            else:
                count = 1
                temp = arr[i]
            
            if(max_ele < count):
                
                max_ele = count
                ele = arr[i]
                
                if(max_ele > (n//2)):
                    flag = 1
                    break
            
            
        if(flag == 1):
            return ele
        elif(len(arr) == 1):
            return arr[0]
        else:
            return -1
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
    
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends