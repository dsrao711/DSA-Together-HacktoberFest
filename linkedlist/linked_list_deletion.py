# node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# class LinkedList

class LinkedList:
    def __init__(self):
        self.head = None
    # Add new element at the end of the list
    def push_back(self, newElement):
        newNode = Node(newElement)
        if(self.head == None):
            self.head = newNode
            return
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode

    # Delete First node of the list
    def pop_front(self):
        self.head = self.head.next

    # Delete Last Node
    def lastNode(self):
        if(self.head != None):
            if(self.head.next == None):
                self.head = None
            else:
                temp = self.head
                while(temp.next.next != None):
                    temp = temp.next
                temp.next = None

        # Delete Any Node from the linked list

    def DeleteNode(self, position):
        if(position < 1):
            print("Position should be greater than one")
        elif(position == 1 and self.head != None):
            self.head = self.head.next
        else:
            temp = self.head
            for i in range(1, position-1):
                if(temp != None):
                    temp = temp.next

            if(temp != None and temp.next != None):
                temp.next = temp.next.next
                
            else:
                print("The node is already null")

    # display the content of the list

    def PrintList(self):
        temp = self.head
        if(temp != None):
            print("\nThe list contains:", end=" ")
            while (temp != None):
                print(temp.data, end=" ")
                temp = temp.next
        else:
            print("\nThe list is empty.")


# test the code
MyList = LinkedList()

# Add four elements in the list.
MyList.push_back(10)
MyList.push_back(20)
MyList.push_back(30)
MyList.push_back(40)
MyList.push_back(80)
MyList.push_back(90)
MyList.push_back(50)
MyList.PrintList()

# Delete the first node
MyList.pop_front()
MyList.PrintList()

# Delete Last Node

MyList.lastNode()
MyList.PrintList()

# Delete element at position 2

MyList.DeleteNode(2)
MyList.PrintList()