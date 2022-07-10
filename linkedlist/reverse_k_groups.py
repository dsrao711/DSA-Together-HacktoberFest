# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        curr = head
        for _ in range(k):
            if not curr: 
                return head
            curr = curr.next
        
        prev = None
        curr = head
        next = None
        count = 0
            
        # Step 1 : Reverse k nodes 
        while(curr != None and count < k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1
            
        # Step 2 : Recursion 
        if(next != None):
            head.next = self.reverseKGroup(next , k)
            
        # Step 3 : Return 
        return prev