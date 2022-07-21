# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = []
        q.append([root , 0])
        op = []
        
        while(q):
            node , level = q.pop(0)
            
            if(node) :
                if(len(op) < level + 1):
                    op.append([])
                op[level].append(node.val)
                q.append([node.left , level + 1])
                q.append([node.right, level + 1])
        
        return op