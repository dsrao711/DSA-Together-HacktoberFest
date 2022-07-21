#User function Template for python3
import collections

class Solution:
    def bottomView(self, root):
        # code here
        q = []
        m = {}
        q.append([root , 0])
        
        while(q):
            node , hd = q.pop(0)
            if(node):
                m[hd] = node.data
                if(node.left):
                    q.append([node.left , hd - 1])
                if(node.right):
                    q.append([node.right , hd + 1])

        m = collections.OrderedDict(sorted(m.items()))
        return m.values()
    
    