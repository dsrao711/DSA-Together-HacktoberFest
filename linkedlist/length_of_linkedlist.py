class Node :
    def __init__ (self , data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def insertNode(self , value):
        newNode  = Node(value)
        newNode.next = self.head
        self.head = newNode

    def getLength(self) :
        temp = self.head
        count = 0 
        while(temp):
            count += 1
            temp = temp.next
        return count
    
if __name__ == '__main__':
    MyList = LinkedList()
    MyList.insertNode(10)
    MyList.insertNode(20)
    MyList.insertNode(30)
    MyList.insertNode(40)
    MyList.insertNode(50)
    len_list = MyList.getLength()
    print("Length of the Linked List is : " , len_list)
