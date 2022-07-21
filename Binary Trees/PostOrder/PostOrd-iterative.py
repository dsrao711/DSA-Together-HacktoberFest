# 1 stack 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        op = []
        stack = []
        curr = root
        while(stack or curr):
            # check for left nodes until leftmost is found
            if(curr):
                stack.append(curr)
                curr = curr.left  
            # Check for right nodes of the curr leftmost node
            else:
                temp = stack[-1].right
                # if no right child present , it means end of tree has reached
                if(temp == None):
                    # append in the op
                    temp = stack[-1]
                    stack.pop()
                    op.append(temp.val)
                    # check if the popped element is the right child of top of stack
                    # if no the top of the stack has a right side to be traversed
                    # if yes , pop out and append in the op
                    while(stack and temp == stack[-1].right):
                        temp = stack[-1]
                        stack.pop()
                        op.append(temp.val)
                # if right child present , repeat the same process on that node by making it
                # curr
                else:
                    curr = temp    
        return op
                




# 2 stacks
# https://youtu.be/2YBhNLodD8Q
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        "Using 2 stacks"
        
        op = []
        s1 = deque()
        s2 = deque()
        
        if(root == None):
            return op
        # append the root in s1
        s1.append(root)
    
        while(s1):
            # Add the top of stack in stack 2 and check for its left and right nodes
            root = s1.pop()
            s2.append(root.val)
            if(root.left):
                s1.append(root.left)
            if(root.right):
                s1.append(root.right)
                
        while(s2):
            op.append(s2.pop())
        return op
        
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def postorderTraversal(self, root) :
      
      if root == None:
        return
      
      stack = deque()
      stack.append(root)

      # create another stack to store postorder traversal
      out = deque()

      # loop till stack is empty
      while stack:

          # pop a node from the stack and push the data into the output stack
          curr = stack.pop()
          out.append(curr.val)

          # push the left and right child of the popped node into the stack
          if curr.left:
              stack.append(curr.left)

          if curr.right:
              stack.append(curr.right)
              
      out.reverse()
      
      return out
    
    
#https://www.youtube.com/watch?v=kcTcfOWFizA

# 