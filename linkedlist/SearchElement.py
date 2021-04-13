class Node :
    def __init__(self , data):
        self.data = data
        self.next = None
    
class LinkedList :
    def __init__ (self):
        self.head = None

    def insertNode(self , value) :
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode

    def SearchElement (self, element):
        temp = self.head
        while(temp != None):
            if (temp.data == element):
                return True
            temp = temp.next
        return False


if __name__ == '__main__' : 
    MyList = LinkedList()
    MyList.insertNode(12)
    MyList.insertNode(13)
    MyList.insertNode(14)
    MyList.insertNode(15)
    MyList.insertNode(16)
    if (MyList.SearchElement(16) == True):
        print ("Yes")
    else:
        print("No")
        