
import collections
class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        # code here
        if(root == None):
            return 0
        q = []
        m = {}
        q.append([root , 0])
        while(q):
            node , hd = q.pop(0)
            if(node):
                if(hd not in m):
                    m[hd] = node.data
                if(node.left):
                    q.append([node.left , hd - 1])
                if(node.right):
                    q.append([node.right , hd + 1])
        
        m = collections.OrderedDict(sorted(m.items()))
        
        return m.values()
        
        
    

