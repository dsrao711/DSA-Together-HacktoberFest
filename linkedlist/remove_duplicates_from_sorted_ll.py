# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
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


# better solution : https://practice.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1

def removeDuplicates(head):
    #code here
    curr = head
    if(head == None or head.next == None):
        return 
    
    while(curr.next):
        if(curr.data == curr.next.data):
            curr.next = curr.next.next
        else:
            curr = curr.next
            
    return curr