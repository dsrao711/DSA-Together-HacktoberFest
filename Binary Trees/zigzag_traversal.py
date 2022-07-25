# 

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to store the zig zag order traversal of tree in a list.
    def zigZagTraversal(self, root):
        
        if(root == None):
            return 

        flag = False 
        q = []
        q.append(root)
        op = []
        
        while q :
            level = []
            n = len(q)
            for i in range(n):
                node = q.pop(0)
                level.append(node.data)
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
            flag = not flag
            if(flag == False):
                level = level[::-1]
            for i in range(len(level)):
                op.append(level[i])
        
        return op
                
            
            
            