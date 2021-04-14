class Node :
    def __init__ (self, data ) :
        self.data = data
        self.prev = None
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

# Insert a node at the beginning 


    def InsertAtBeg(self , value):
        newNode = Node(data = value)
        newNode.prev = None
        newNode.next = self.head

        if(self.head is not None):
            self.head.prev = newNode
        
        self.head = newNode

    def InsertAtPos(self , value , prevNode) :
        newNode = Node(data = value)
        newNode.next = prevNode.next
        prevNode.next = newNode
        newNode.prev = prevNode
        if(newNode is not None) :
            newNode.next.prev = newNode

    def InsertAtEnd (self , value ):
        newNode = Node(data = value)
        newNode.next = None
        #For Empty Linked List 
        if(self.head is None):
            newNode.prev = None
            self.head = newNode
            return

        lastNode = self.head
        while(lastNode.next is not None):
            lastNode = lastNode.next
        lastNode.next = newNode
        newNode.prev = lastNode

    

if __name__ == '__main__':
    head = None
    head = 