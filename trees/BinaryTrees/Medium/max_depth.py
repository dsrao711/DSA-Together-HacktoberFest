# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# REcursive
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if(root == None):
            return 0
        # Recursive
        return 1 + max(self.maxDepth(root.left) , self.maxDepth(root.right))
    
    