class Node :
    def __init__ (self, data ) :
        self.data = data
        self.prev = None
        self.next = None
    
class DoublyLinkedList:
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

    def InsertBefore(self , head_ref , nextNode , value) :
        newNode = Node(value)
        if(nextNode == None):
            print("Next Node is Null")
        
        newNode.prev = nextNode.prev
        nextNode.prev = newNode
        newNode.next = nextNode

        if(newNode.prev !=  None):
            newNode.prev.next = newNode
        else:
            head_ref = newNode
        return head_ref


    def PrintList(self , node) :
        while node :
            print(node.data)
            node = node.next
    



Mylist = DoublyLinkedList()
Mylist.InsertAtEnd(10)
Mylist.InsertAtEnd(20)
Mylist.InsertAtEnd(30)
Mylist.InsertAtEnd(40)
Mylist.InsertAtEnd(50)

Mylist.InsertAtBeg(22)
Mylist.InsertAtPos(3 , Mylist.head.next)


Mylist.PrintList(Mylist.head)

Mylist.InsertBefore(Mylist.head , Mylist.head.next , 12)

Mylist.PrintList(Mylist.head)
