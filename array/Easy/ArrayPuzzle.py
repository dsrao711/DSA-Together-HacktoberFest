#  https://practice.geeksforgeeks.org/problems/product-array-puzzle4525/1/

class Solution:
    def productExceptSelf(self, nums, n):
        #code here
        totalProduct = 1
        if(0 in nums):
            
            # Find the index with 0 value
            index = nums.index(0)
            # nums[index] == 0
            nums[index] = 1
            for i in range(0 , n):
                totalProduct *= nums[i]
            # Rest all values will be 0
            op = [0]*n
            op[index] = totalProduct
            
            return op
            
        else:
            
            for i in range(0 , n):
                totalProduct *= nums[i]
            
            for j in range(0 , n):
                nums[j] = int(totalProduct / nums[j])
        
            return nums 
                
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=Solution().productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends