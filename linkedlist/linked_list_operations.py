class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList :
    def __init__(self):
        self.start = None

# View List 

    def viewList(self):
        if self.start == None : 
            print("List is empty")
        else:
            temp = self.start
            while(temp != None):
                print(temp.data , end = " ")
                temp = temp.next

#Insert a Node at the End
    def insertLast (self , value):
        newNode = Node(value)
        if(self.start == None):
            self.start = newNode
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = newNode

# Delete a node 
    def DeleteFirst(self):
        if(self.start == None):
            print("Linked List is empty")
        else :
            self.start = self.start.next 

if __name__ == '__main__' :
    MyList = LinkedList()
    MyList.insertLast(10)
    MyList.insertLast(20)
    MyList.insertLast(30)
    MyList.insertLast(40)
    MyList.viewList()
    MyList.DeleteFirst()
    MyList.viewList()
    print()
    input()