# https://leetcode.com/problems/sliding-window-maximum/submissions/
# Ref : https://youtu.be/MCvGwtkqJS0
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        
        n = len(nums)
        # Deq for storing indices 
        deq = deque()
        op = []
        j = 0 

        # 1. Remove previous index at the front
        # 2. Remove useless elements at the rear
        # 3. Add useful element if found in the deq
        # 4. Update the deq
        
        # A new window is basically removing the oldest element and adding a new incoming ele
        
        # Fill the deque for first window 
        for i in range(0 , k):
            j = i 
            # if the incoming element is lesser than the last ele of deq , its useless 
            while(deq and nums[deq[-1]] <= nums[i]):
                deq.pop()
            deq.append(i)
            
        # Start iteration from second window 
        for i in range(j , n):
            # Previous index 
            while(deq and deq[0] <= i - k):
                deq.popleft()
            # Useless elements at the rear
            while(deq and nums[deq[-1]] <= nums[i]):
                deq.pop()
            # Append useful element
            deq.append(i)
            # Update result
            op.append(nums[deq[0]])
            
        return op
        