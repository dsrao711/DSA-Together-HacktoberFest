# Link : https://leetcode.com/problems/range-sum-of-bst/submissions/

#Approach 1 : Stacks 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        
        st = [root]
        
        range_sum = 0
        
        while(st):
          curr = st.pop()
          if curr :
              
            # Check if node is in range
            if (curr.val >= low and curr.val <= high):
              range_sum += curr.val
                
            # If only greater than low , then traverse left 
            if (curr.val > low):
              st.append(curr.left)
              
            # If only less than high , then traverse right 
            if (curr.val < high):
              st.append(curr.right)
              
        return range_sum
              
        