# https://leetcode.com/problems/daily-temperatures/submissions/

"""

We are supposed to return the number of positions required for a higher temperature than the current
temp . 

Since we need the index values , we will be using enumerates in Python 

Enumerates in Python
        
        Eg : "Divya"
        For enumerate("Divya") = [(0 , 'D') , (1 , 'i') , (2 , 'v') , (3 , 'y') , (4 , 'a' )]
        

So , 

Lets say the index number = Curr_Day 
             temp = Curr_Temp 
     
     
We keep on appending the index numbers in the stack 
While appending , we check if the top element of the stack is lesser than the curr_temp
If yes , we have found a greater element , so we store the difference of index number of these two elements
and store it in the op array 

If a greater element is not found , we keep on appending these elements in the stack unless next greater
ele is found


"""


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        op = [0]*n
        stack = []
        
        for curr_day , curr_temp in enumerate(temperatures):
            # Check with top of stack
            while stack and temperatures[stack[-1]] < curr_temp :
                # Pop out the top
                prev_day = stack.pop()
                # Store the difference in op array
                op[prev_day] = curr_day - prev_day
                
            # Else push the curr_day until the next greater temp is not found
            stack.append(curr_day)
            
        return op
            