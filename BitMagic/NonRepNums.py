
# https://practice.geeksforgeeks.org/problems/finding-the-numbers0215/1/?problemStatus=unsolved&page=1&company[]=Accolite&category[]=Bit%20Magic&query=problemStatusunsolvedpage1company[]Accolitecategory[]Bit%20Magic#


# Naive approach -1 
# O(nlogn) - Time complexity
class Solution:
    def singleNumber(self, nums):
        # Code here
        nums.sort()
        op = []
        i = 0
        while(i < len(nums)):
            
            if(nums[i] == nums[i-1]):
                
                nums[i] = 0
                nums[i-1] = 0
            i += 1
                
        nums.sort()
        return nums[-2:]
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        v = list(map(int,input().split()))
        ob = Solution();
        ans = ob.singleNumber(v)
        for i in ans:
            print(i, end = " ")
        print()

# } Driver Code 
# 

# https://www.geeksforgeeks.org/find-two-non-repeating-elements-in-an-array-of-repeating-elements/