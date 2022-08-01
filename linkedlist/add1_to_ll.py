# https://practice.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1


class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    def addOne(self,head):
        #Returns new head of linked List.
        
        curr = head
        s = ""
        
        if(head == None):
            return 
        
        while(curr):
            s = s + str(curr.data)
            curr = curr.next 
            
        s = str(int(s) + 1)
        node = Node(int(s))
        return node

        