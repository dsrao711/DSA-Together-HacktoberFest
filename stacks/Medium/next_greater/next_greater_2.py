#https://leetcode.com/problems/next-greater-element-ii/

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        stack=[]
        rst= [-1]*len(nums)
        
        for i in range(len(nums)-2,-1,-1):
            # POP
            while stack and nums[i]>=stack[-1]:
                stack.pop()  
            # PUSH  
            stack.append(nums[i]) 
        
        for i in range(len(nums)-1,-1,-1):
            # POP
            while stack and nums[i]>=stack[-1]:
                stack.pop()
            # ANSWER
            if stack:
                rst[i]=stack[-1]
            # PUSH
            stack.append(nums[i])
        
        return rst