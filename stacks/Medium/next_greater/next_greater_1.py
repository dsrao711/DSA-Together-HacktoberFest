#https://leetcode.com/problems/next-greater-element-i


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        # stack for comparison
        stack = []
        # dict for storing next greater element for all the elements of 
        # nums2
        
        d = {}
        
        for num in nums2:
          # Check if the num if greater than the top of the stack 
          # If yes , we found the next greater element for the num
          
          while(stack and stack[-1] < num):
            top = stack.pop()
            d[top] = num
            
          # If the stack is empty or if the num is not greater than the 
          # top of the stack , append the elements in the stack
          if not stack or stack[-1] > num:
            stack.append(num)
            
        # These are the elements which dont have a next greater ele , 
        # In this case , just pop out the elements and store it in the 
        # dict with value -1 
        
        while(stack):
          rem = stack.pop()
          d[rem] = -1
          
        # Since , nums1 is a subset of nums2 , return the elements from 
        # dict d , which are present in nums1
        
        return [d[i] for i in nums1]
          
        
        
        
        
        
  
          