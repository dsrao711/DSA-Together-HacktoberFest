# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# remove loop , return starting point of loop

class Solution(object):
    def checkCycle(self , head ):
        slow = head
        fast = head
        while(fast != None and fast.next != None):
            slow = slow.next 
            fast = fast.next.next
            
            if(slow == fast):
                return slow
        return None
        
    def detectCycle(self, head):
        
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        meet = self.checkCycle(head)
        if(meet  == None):
            return None
        
        start = head
        
        while(start != meet):
            start = start.next
            meet = meet.next
        
        return start
    
    
        
        
            
            
            