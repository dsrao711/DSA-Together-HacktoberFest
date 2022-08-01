# https://www.codingninjas.com/codestudio/problems/let-last-be-the-first_920455?leftPanelTab=1

'''
Following is the Linked list class structure already written

class LinkedListNode:
    
	def __init__(self, data):
		self.data = data
		self.next = None
'''


def moveToFront(head):

	# Write your code here.
    curr = head 
    sec_last = None
    
    if (head == None or head.next == None):
        return head
    
    while(curr and curr.next):
        sec_last = curr
        curr = curr.next
        
    sec_last.next = None
    curr.next = head
    head = curr
    
    return curr
    
