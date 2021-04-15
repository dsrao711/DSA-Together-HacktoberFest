# Traversal of Circular Linked List

class Node:

    def __init__(self , data):
        self.data = data
        self.next = None
class CircularLinkedList :

    def __init__(self):
        self.head = None

    def InsertNode(self , value):
        newNode = Node(value)
        # Adding a new node in the beginning 
        newNode.next = self.head
        temp = self.head

        # Store the address of new node in the last node

        if(self.head is not None):
            while(temp.next != self.head):
                temp = temp.next
            temp.next = newNode
        else :
            newNode.next = newNode

        self.head = newNode

    def InsertAfter (self , data , )

    def PrintList (self):
        temp = self.head
        if(self.head is not None):
            while(True):
                print(temp.data)
                temp = temp.next

                if(temp == self.head):
                    break

MyList = CircularLinkedList()
MyList.InsertNode(22)
MyList.InsertNode(32)
MyList.InsertNode(42)
MyList.InsertNode(52)
MyList.InsertNode(62)

MyList.PrintList()