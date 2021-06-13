#https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem


class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)
    

    def insertion(self,cur,val):
      
      if not cur: 
          cur = Node(val)
          
      elif cur.info > val: 
          cur.left = self.insertion(cur.left, val)
          
      else: 
          cur.right = self.insertion(cur.right, val)
      return cur
        
        
        
        
    def insert(self, val):
        #Enter you code here.
        if not self.root:
          self.root = Node(val)
        else:
          self.insertion(self.root,val)
          
                
        
        
        
      
        

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)


#Leetcode : 
#https://leetcode.com/problems/insert-into-a-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def insert(root,x):
          if(root):
            if(x < root.val):
              # Insert Left
              # If Left node is already present
              if(root.left):
                insert(root.left,x)        
              #Else, create a new left node
              else:
                root.left = TreeNode(x)
            else:
              # Insert Right
              # If Right node is already present
              if(root.right):
                insert(root.right , x)
              # Else , create a new right node
              else:
                root.right = TreeNode(x)
                
          else:
            return root
            
        if not root:
          return TreeNode(val)
        
        insert(root , val)
        
        return root
                
              
          