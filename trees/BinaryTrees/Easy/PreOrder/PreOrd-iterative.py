
#https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def preorderTraversal(self, root):
        stack = deque()
        op = []
        # Root - Left - Right
        if(root == None):
          return
        # Append the root
        stack.append(root)  
        while stack:
          # Print the root 
          curr = stack.pop()
          op.append(curr.val)
          # Since first left is printed then right , right node will be stored first 
          # in the stack and the left one as stack follows LIFO 

          # Check for right
          if(curr.right):
            stack.append(curr.right)  
          # Check for left 
          if(curr.left):
            stack.append(curr.left)
            
        return op
          
# TC : O(n)
# SC : O(n)
# ref :  https://youtu.be/Bfqd8BsPVuw