# https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing elements of left view of the binary tree.
def util(root , op , level):
    if(root == None):
        return 0
    if(len(op) < level):
        op.append(root.data)
    util(root.left , op , level + 1)
    util(root.right , op , level + 1)
    
    
def LeftView(root):
    op = []
    util(root , op , 1)
    return op
    







