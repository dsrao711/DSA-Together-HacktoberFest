
# Link : https://leetcode.com/problems/kth-smallest-element-in-a-bst/solution/

#Approach 1 : Using recursion - Inorder traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
      
    def kthSmallest(self, root: TreeNode, k: int) -> int:
      
      def inorder(r):
        return inorder(r.left) + [r.val] + inorder(r.right) if r else []
      
      return inorder(root)[k-1]
      
    

# Approach 2 : Using stacks

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right