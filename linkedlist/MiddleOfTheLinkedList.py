# Link to the problem : https://leetcode.com/problems/middle-of-the-linked-list/

class Solution:    
    # Solution using 2 Pointers 
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:         
        if not head or not head.next: 
            return head
        slow=head
        fast=head
        # Moving slow pointer by one and fast pointer by two. 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            if fast: 
                fast = fast.next
        return slow
        # When fast pointer reaches the end, slow pointer reaches the middle of the linked list.

# Time Complexity : O(N)