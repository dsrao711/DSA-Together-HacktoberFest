20. Reverse a Doubly Linked list.
Here is a simple method for reversing a Doubly Linked List. 
All we need to do is swap prev and next pointers for all nodes, change prev of the head (or start) and change the head pointer in the end.
* Function to reverse a Doubly Linked List */ 
 
 
Time Complexity: O(N), where N denotes the number of nodes in the doubly linked list. 
Auxiliary Space: O(1) 
    We can also swap data instead of pointers to reverse the Doubly Linked List. 
    Method used for reversing array can be used to swap data. Swapping data can be costly compared to pointers if the size of the data item(s) is more. Method 2: The same question can also be done by using Stacks. Steps:
1. Keep pushing the node’s data in the stack. -> O(n) 
2. The keep popping the elements out and updating the Doubly Linked List *Function to reverse a Doubly Linked List using Stacks * Function to reverse a Doubly Linked List using Stacks */ 
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
 
 
class DoublyLinkedList:
     # Constructor for empty Doubly Linked List
    def __init__(self):
        self.head = None
 
    # Function reverse a Doubly Linked List
    def reverse(self):
        temp = None
        current = self.head
 
        # Swap next and prev for all nodes of
        # doubly linked list
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
 
        # Before changing head, check for the cases like
        # empty list and list with only one node
        if temp is not None:
            self.head = temp.prev
 
    # Given a reference to the head of a list and an
    # integer,inserts a new node on the front of list
    def push(self, new_data):
 
        # 1. Allocates node
        # 2. Put the data in it
        new_node = Node(new_data)
 
        # 3. Make next of new node as head and
        # previous as None (already None)
        new_node.next = self.head
 
        # 4. change prev of head node to new_node
        if self.head is not None:
            self.head.prev = new_node
 
        # 5. move the head to point to the new node
        self.head = new_node
 
    def printList(self, node):
        while(node is not None):
            print node.data,
            node = node.next
 
 
# Driver code
dll = DoublyLinkedList()
dll.push(2)
dll.push(4)
dll.push(8)
dll.push(10)
 
print "\nOriginal Linked List"
dll.printList(dll.head)
 
# Reverse doubly linked list
dll.reverse()
 
print "\n Reversed Linked List"
dll.printList(dll.head)
             
                  Time Complexity: O(N) 
                  Auxiliary Space: O(N)
 In this method, we traverse the linked list once and add elements to the stack, and again traverse the whole for updating all the elements. The whole takes 2n time, which is the time complexity of O(n)
