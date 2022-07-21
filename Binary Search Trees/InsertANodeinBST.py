# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        def insert(parent,data):
            
            if( parent is None):
                parent = TreeNode(data)
            
            if(parent.val > data): # Left side
                # If node is not present , create new Node
                if( parent.left is None):
                    parent.left = TreeNode(data)
                # Else, insert
                else:
                    insert(parent.left,data)
                    
            if(parent.val < data): #Right
                # If node is not present, create new Node
                if(parent.right is None):
                    parent.right = TreeNode(data)
                # Else, create a new Node
                else:
                    insert(parent.right,data)
             
            return parent
            
        
        return insert(root,val)