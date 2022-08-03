# https://practice.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1

class Solution:
    def isPalindrome(self, head):
        curr = head
        s = ""
        
        if(head == None):
            return 
        
        while(curr):
            s = s + str(curr.data)
            curr = curr.next
        if(s == s[::-1]):
            return True
        else:
            return False
        