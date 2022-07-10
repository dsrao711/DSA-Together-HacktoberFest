# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        curr = head
        
        if(curr == None):
            return None
        
        if(curr.next != None):
            if(curr.val == curr.next.val):
                curr.next = curr.next.next
                self.deleteDuplicates(curr)
            else:
                self.deleteDuplicates(curr.next)
        
        return curr