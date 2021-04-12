class Node : 
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None

    def InsertAtEnd(self , value):
        newNode = Node(value)
        if self.start == None:
            self.start = newNode
            return
        else :
            temp = self.start
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode

    def Insert(self , position , value):
        newNode = Node(value)
        if position < 1 :
            print("Position must be greater than 0")
        #Insertion at beginning 
        elif position == 1 : 
            newNode.next = self.start
            self.start = newNode

        else :
            temp = self.start
            for i in range(0 , position - 1) :
                if(temp.next != None):
                    temp = temp.next
            if (temp != None):
                newNode.next = temp.next
                temp.next = newNode
            else:
                print("\n Previous node was null")
            
# Display the content of the list 

    def PrintList(self):
        temp = self.start
        if (temp != None):
            while(temp != None):
                print(temp.data)
                temp = temp.next
        else :
            print("Linked list is empty")

MyList = LinkedList()

MyList.InsertAtEnd(10)
MyList.InsertAtEnd(20)
MyList.InsertAtEnd(30)
MyList.InsertAtEnd(40)

MyList.PrintList()

MyList.Insert(2,100)
MyList.PrintList()
