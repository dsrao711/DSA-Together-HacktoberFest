#https://practice.geeksforgeeks.org/problems/circular-linked-list/1

class Node:
 
    def __init__(node, data):
        node.data = data 
        node.next = None 
 
class LinkedList:
    
    def __init__(node):
        node.head = None
 
#function to check if the list is circular
def IsCircular(head):
    if head==None:
        return True
         
    temp = head.next
     
    # condition to stop the loop since we dont need an infinite loop. It will either reach end of list or the head of list
    while((temp is not None) and (temp is not head)):
        temp = temp.next
     
    return(temp==head)
 
 
#main funtion
if __name__=='__main__':
    new_list = LinkedList()
    new_list.head = Node(0)
    node2 = Node(1)
    node3 = Node(2)
    node4 = Node(3)
     
    new_list.head.next = node2
    node2.next = node3
    node3.next = node4
     
    if (IsCircular(new_list.head)):
        print('True')
    else:
        print('False')
     
# connected node4 to the list and formed a cycle, so the program should now return a True 
    node4.next = new_list.head
     
    if (IsCircular(new_list.head)):
        print('True')
    else:
        print('False')

#Time Complexity : O(n) where n is number of nodes in list