#https://leetcode.com/problems/merge-two-sorted-lists/

# Recursive method

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if l1 is None:
                return l2
        if l2 is None:
            return l1

        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2) # l1 will be the new head and the rest is to be merged
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1) # l2 will be the new head and the rest is to be merged
            return l2
        
        
        
        
        
        
        