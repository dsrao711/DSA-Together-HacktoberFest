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

    # Store last and second last node in curr and sec_last respectively 
    while(curr and curr.next):
        sec_last = curr
        curr = curr.next
    
    # Make secondlast point to null
    sec_last.next = None
    # Last pointing to first node
    curr.next = head
    # New head is curr 
    head = curr
    
    return curr
    
