# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def height(self , root):
        if(root == None):
            return 0
        return max(self.height(root.left) , self.height(root.right)) + 1
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if(root == None):
            return True
        rh = self.height(root.right)
        lh = self.height(root.left)
        
        r = self.isBalanced(root.right)
        l = self.isBalanced(root.left)
        
        if abs(lh - rh) <= 1:
            return l and r
        
        return False
        
        
        