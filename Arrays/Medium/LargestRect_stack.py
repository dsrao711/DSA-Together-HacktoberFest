
# https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    
    def largestRectangleArea(self, h) :
        
        n = len(h)
        left_index = [0]*n
        right_index = [0]*n
        stack = []
        
        # Calculate the left indices to store the next smallest element for each bar in the histogram

        
        for i in range(0 , n):
        # If the stack is empty -> left_index = 0 since there is no element remaining to the left of the bar in the histogram
          if(len(stack) == 0):
            left_index[i] = 0
          else:
            # If the left element to the bar is greater than bar , keep popping out until an element smaller than the bar is found
            while(len(stack) != 0 and h[stack[-1]] >= h[i]):
              stack.pop()
            if(len(stack) == 0):
              left_index[i] = 0
            else:
            # Store the top most element i.e the next smallest element in the left_index
              left_index[i] = stack[-1] + 1
          stack.append(i)
          
        # Clear the stack 
        
        while(len(stack)!= 0):
          stack.pop()
        
        # Calculate the left indices to store the next smallest element for each bar in the histogram
        
        for i in range(n-1 , -1 , -1):
        # If the stack is empty -> right index = n -1  since there is n -1 element remaining to the right side  of the bar in the histogram greater than the bar
          if(len(stack) == 0):
            right_index[i] = n - 1
          else:
            while(len(stack) != 0 and h[stack[-1]] >= h[i]):
              stack.pop()
            if(len(stack) == 0):
              right_index[i] = n - 1
            else:
              right_index[i] = stack[-1]- 1
          stack.append(i)
        
        # Contains the max are 
        max_area = 0
        
        for i in range(0 , n):
          
          max_area = max(max_area , (right_index[i] - left_index[i] + 1)*h[i])
          
        return max_area
        
        # Calc area using left , right and height indexs
        

# Time Comp = O(n)