# https://leetcode.com/problems/linked-list-cycle/submissions/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Implementing Floyd cycle detection algo
class Solution(object):
    
    def hasCycle(self, head):
        
        """
        :type head: ListNode
        :rtype: bool
        """
    
        fastPointer = head
        slowPointer = head
        
        while(fastPointer != None and slowPointer != None and fastPointer.next != None):
            slowPointer = slowPointer.next 
            fastPointer = fastPointer.next.next
            if(slowPointer == fastPointer) : 
                return True
        
        return False