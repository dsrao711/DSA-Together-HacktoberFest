#https://leetcode.com/problems/sliding-window-maximum/submissions/
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        
        deq = deque()
        op = []
        # Deque
        for i in range(0 , len(nums)):    
        # Clean the deque
        # 1. remove the elements from front which are out of range
            if(len(deq) != 0 and deq[0] == i - k):
                deq.popleft()
            
        # 2. remove the ele from rare which are less than incoming ele
            while(len(deq) and nums[deq[-1]] <= nums[i]):
                deq.pop()
        # push the incoming element 
            deq.append(i)
        # since the deque is stored in decreasing order , the
        # frontmost element is the largest value possible 
        # pop the front ele and store in op 
            if(i >= k-1):
                op.append(nums[deq[0]])
        return op
        