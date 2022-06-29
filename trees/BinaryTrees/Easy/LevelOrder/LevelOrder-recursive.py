# Link to the problem : https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Recursive approach 

class Solution:
    def levelOrder(self, root) :
      result = []
      self.TreeTraversal(root,0,result)
      return result
        
    def TreeTraversal(self,node,level,result):
      if(node == None):
        return 
      
      if(len(result) < level + 1) :
        result.append([])
        
      result[level].append(node.val)
      self.TreeTraversal(node.left , level+1 , result)
      self.TreeTraversal(node.right , level+ 1 , result)