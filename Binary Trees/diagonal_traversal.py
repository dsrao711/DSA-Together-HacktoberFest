# https://practice.geeksforgeeks.org/problems/diagonal-traversal-of-binary-tree/1
'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
#Complete the function below
class Solution:
    def diagonal(self,root):
        #:param root: root of the given tree.
        #return: print out the diagonal traversal,  no need to print new line
        #code here
        op = []
        q = []
        node = root 
        while(node):
            op.append(node.data)
            if(node.left):
                q.append(node.left)
            if(node.right):
                node = node.right
            else:
                if(len(q) >= 1):
                    node = q.pop(0)
                else:
                    node = None
        return op
        
