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
            

# Better approach  : https://practice.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, head1, head2):
        # code here
        # return head of sum list
        curr1 = head1
        curr2 = head2
        
        s1 = ''
        s2 = ''
        
        
        if(head1 == None and head2 == None):
            return 
        
        if(head1 == None):
            return head2
        
        if(head2 == None):
            return head1
            
        while(curr1):
            s1 = s1 + str(curr1.data)
            curr1 = curr1.next
        
        while(curr2) : 
            s2 = s2 + str(curr2.data)
            curr2 = curr2.next
        
        ans = str(int(s1) + int(s2))
        node = Node(0)
        
        curr = node 
        for i in ans : 
            curr.next = Node(i)
            curr = curr.next 
        
        return node.next
            