#https://leetcode.com/problems/reverse-linked-list/

# Iterative method

#Approach : 

# Store the head in a temp variable called current . 

#   curr = head , prev = null 

# Now for a normal linked list , the current will point to the next node and so on till null 
# For reverse linked list, the current node should point to the previous node and the first node here will point to null 

# Keep iterating the linkedlist until the last node and keep changing the next of the current node to prev node and also 
# update the prev node to current node and current node to next node


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        curr = head
        prev = None
        while(curr != None):
          # next - The node which is moving forward till the end of linkedlist
          next = curr.next
          # The next pointer of the current node should point to the prev node 
          curr.next = prev
          # update the prev node 
          prev = curr
          # update the curr to next 
          curr = next
          
        return prev
          
# Approach (Recursive):

# Divide the linked list to two halved
# First half is head and the remaining as rest 
# The head points to the rest in a normal linked list 
# In the reverse linked list , the next of current points to the prev node and the head node should point to NULL
# Keep continuing this process till the last node 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        if head is None or head.next is None:
          return head
        rest = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return rest