# Link : https://leetcode.com/problems/invert-binary-tree/submissions/

# YT Link : https://www.youtube.com/watch?v=OnSn2XEQ4MY



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def invertTree(self, root):
        
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        #  Edge cases
        if not root:
          return None
        
        # Swap the children
        temp = root.left 
        root.left = root.right
        root.right = temp
        
        # Recursively do it for all nodes
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root