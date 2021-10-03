# Implementing stack using Linked list

class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Stack :
    
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        if (self.head == None):
            print("Stack is Empty")
        else:
            print("Stack is not empty")
    
    def push(self , data):
        newNode = Node(data)
        if (self.head == None):
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
            
    def pop(self):
        if self.isEmpty():
            return None
        else:
            poppedNode = self.head
            self.head = self.head.next
            poppedNode = None
            return poppedNode.data
        
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.head.data
        
    def print(self):
        if self.isEmpty():
            return None
        else:
            temp = self.head
            while(temp.next != None):
                print(temp.data)
                temp = temp.next
            return

MyStack = Stack()
MyStack.push(11)
MyStack.push(22)
MyStack.push(33)
MyStack.push(44)
 
# Display stack elements
MyStack.print()
 
# Print top element of stack
print("\nTop element is ",MyStack.peek())
 
# Delete top elements of stack
MyStack.pop()
MyStack.pop()
 
# Display stack elements
MyStack.print()
 
# Print top element of stack
    
            
    