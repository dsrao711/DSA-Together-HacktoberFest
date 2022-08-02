#User function Template for python3

''' structure of node:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

'''

def pushNode(add, data):
    new_node = Node(0)
    new_node.data = data
    new_node.next = (add)
    (add) = new_node
    return add
    
    
def findIntersection(head1,head2):
    
    p1 = head1 
    p2 = head2 
   
    dummy = Node(0)
    curr = dummy
    dummy.next = None
    
    if(head1 == None or head2 == None):
        return 

    while(p1 and p2):
        if(p1.data == p2.data):
            curr.next = pushNode((curr.next), p2.data)
            curr = curr.next 
            p1 = p1.next
            p2 = p2.next
        elif(p1.data < p2.data):
            p1 = p1.next
        else:
            p2 = p2.next 

    return dummy.next
