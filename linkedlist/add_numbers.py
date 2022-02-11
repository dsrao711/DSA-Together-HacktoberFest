# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummy = ListNode()
        head1 = l1
        head2 = l2
        curr = dummy 
        carry = 0
        
        while(head1 or head2):
            if(head1 is not None):
                x = head1.val
            else:
                x = 0
                
            if(head2 is not None):
                y = head2.val
            else:
                y = 0 
                
            add = x + y + carry
            carry = add/10
            curr.next = ListNode(add % 10)
            curr = curr.next
            
            if(head1 is not None):
                head1 = head1.next
                
            if(head2 is not None):
                head2 = head2.next
            
        if(carry > 0):
            curr.next = ListNode(carry)
            
        return dummy.next
            