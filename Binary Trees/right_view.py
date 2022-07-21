# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    
    def util(self , root , op , level):
        if(root == None):
            return 0
        if(len(op) < level):
            op.append(root.val)
        self.util(root.right , op , level + 1)
        self.util(root.left , op , level + 1)

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        op = []
        self.util(root , op , 1)
        return op