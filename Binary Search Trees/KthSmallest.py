
# Link : https://leetcode.com/problems/kth-smallest-element-in-a-bst/solution/

#Approach 1 : Using recursion - Inorder traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
      
    def kthSmallest(self, root, k) -> int:
      
      def inorder(r):
        return inorder(r.left) + [r.val] + inorder(r.right) if r else []
      
      return inorder(root)[k-1]
      
    

# Approach 2 : Using stacks
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root, k) -> int:
        stack = []
        # Counter for 
        n = 0
        curr = root
        while(curr or stack):
            # Get all lefts 
            while(curr):
                stack.append(curr)
                curr = curr.left
            # last left possible is reached , check for right nodes if present
            curr = stack.pop()
            # If k is reached , return ans
            n += 1
            if(n == k):
                return curr.val
            curr = curr.right
                
        