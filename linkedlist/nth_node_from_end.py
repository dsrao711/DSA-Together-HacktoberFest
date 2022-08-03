# https://practice.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1

def getNthFromLast(head,n):
    length = 0
    curr1 = head
    curr2 = head
    
    # BC
    if(head == None):
        return 
    # Get the length
    while(curr1):
        length += 1
        curr1 = curr1.next
    
    if(n > length):
        return -1
    else:
        # for length = 8 , 2nd node from end means 6th node from beginning 
        n = length - n
        i = 0

        while(i < n):
            curr2 = curr2.next
            i += 1
            
        return curr2.data
        