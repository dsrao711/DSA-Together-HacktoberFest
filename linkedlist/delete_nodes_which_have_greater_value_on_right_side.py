/* 
Delete nodes which have a greater value on right side using recursion
*/

class Node:
     
    def __init__(self, data, next):
        self.data = data
        self.next = next
 
class LinkedList:
     
    def __init__(self):
        self.head = None
         
    # Function to push a new Node in
    # the linked list
    def push(self, new_data):
     
        new_node = Node(new_data, self.head)
        self.head = new_node
     
    # Function to delete nodes which have a node
    # with greater value node on left side
    def delNodes(self, head):
     
        # Base case
        if head == None:
            return head
         
        global Max
     
        head.next = self.delNodes(head.next)
        if head.data < Max:
            return head.next
         
        Max = max(head.data, Max)
        return head
     
    # Function to print the Linked list
    def printList(self):
         
        curr = self.head
        while curr:
            print(curr.data, end = " ")
            curr = curr.next
        print()
 
# Driver Code
if __name__ == "__main__":
 
    # Start with the empty list
    linkedList = LinkedList()
 
    # Create following linked list
    # 12->15->10->11->5->6->2->3
    linkedList.push(3)
    linkedList.push(2)
    linkedList.push(6)
    linkedList.push(5)
    linkedList.push(11)
    linkedList.push(10)
    linkedList.push(15)
    linkedList.push(12)
 
    print("Given Linked List")
    linkedList.printList()
    Max = float('-inf')
    linkedList.head = linkedList.delNodes(linkedList.head)
 
    print("Modified Linked List")
     
    linkedList.printList()
    
/* 
Sample Outout:

Given Linked List
12 15 10 11 5 6 2 3 
Modified Linked List
15 11 6 3
*/
