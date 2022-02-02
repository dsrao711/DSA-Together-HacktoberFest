# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        c1 = list1
        c2 = list2
        dummy = ListNode()
        prev = dummy
        
        if(list1 == None or list2 == None):
            if(list1 == None):
                return list2
            else:
                return list1
        
        while(c1  and c2 ):
            if(c1.val <= c2.val):
                prev.next = c1
                c1 = c1.next
            else:
                print(c2.val)
                prev.next = c2
                c2 = c2.next
                
            prev = prev.next
            
        prev.next = c1 or c2

        return dummy.next