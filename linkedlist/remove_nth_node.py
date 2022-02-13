# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Fast pointer , slow pointer tech
        dummyhead = ListNode()
        dummyhead.next = head
        fast = dummyhead
        slow = dummyhead
        
        for i in range(0 , n):
            fast = fast.next
        # Difference of n nodes is present between slow and fast
        # Once the fast pointer reaches the end 
        # The slow will be at nth position 
        while(fast.next):
            slow = slow.next
            fast = fast.next
        # Skip the node and point to next of the skipped node
        slow.next = slow.next.next
        
        return dummyhead.next
            