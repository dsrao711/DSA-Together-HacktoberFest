class Node:
      def __init__(self, data):
    self.data = data
    self.next = None
class LinkedList:
  def __init__(self):
    self.head = None

  #Add new element at the end of the list
  def InsertAtEnd(self, newElement):
    newNode = Node(newElement)
    if(self.head == None):
      self.head = newNode
      newNode.next = self.head
      return
    else:
      temp = self.head
      while(temp.next != self.head):
        temp = temp.next
      temp.next = newNode
      newNode.next = self.head

  #Inserts a new element at the given position
  def InsertAtPos(self, newElement, position):     
    newNode = Node(newElement)
    temp = self.head
    NoOfElements = 0
    if(temp != None):
      NoOfElements += 1
      temp = temp.next
    while(temp != self.head):
      NoOfElements += 1
      temp = temp.next
    
    if(position < 1 or position > (NoOfElements+1)):
      print("\nInavalid position.")
    elif (position == 1):
      if(self.head == None):
        self.head = newNode
        self.head.next = self.head
      else:
        while(temp.next != self.head):
          temp = temp.next
        newNode.next = self.head
        self.head = newNode
        temp.next = self.head
    else:
      temp = self.head
      for i in range(1, position-1):
        temp = temp.next 
      newNode.next = temp.next
      temp.next = newNode

  #display the content of the list
  def PrintList(self):
    temp = self.head
    if(temp != None):
      print("The list contains:", end=" ")
      while (True):
        print(temp.data, end=" ")
        temp = temp.next
        if(temp == self.head):
          break
    else:
      print("The list is empty.")

# test the code                  
MyList = LinkedList()

#Add three elements at the end of the list.
MyList.InsertAtEnd(10)
MyList.InsertAtEnd(20)
MyList.InsertAtEnd(30)
MyList.PrintList()

#Insert an element at position 2
MyList.InsertAtPos(100, 2)
MyList.PrintList()

#Insert an element at position 1
MyList.InsertAtPos(200, 1)
MyList.PrintList() 