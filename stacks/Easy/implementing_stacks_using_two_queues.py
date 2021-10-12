
#Link : https://leetcode.com/problems/implement-stack-using-queues/


"""

For a list = [1,2,3,4]

Stack = [1 , 2 , 3 , 4]  -> Top = 4 
Stack.pop = 4

Queue = [1 , 2 , 3 , 4 ] -> FIFO -> First ele = 1

In order to make queue perform stack operations , we need to pop 4 i.e the last element 
We will be using 2 queues here 

POP : 
1) Store all the elements in q1 = [1,2,3,4]
2) Put all the n-1 elements from q1 in q2 such that q1 = [4] , q2 = [1,2,3]
3) Popped element = q1.pop(0) = 4 , q1 = []
4) Now since the last element is popped , make all the positions like before i.e
    q1 = [1,2,3] , q2 = []

Same logic applicable for TOP , no need to put the popped element in q2 as we just need to return the
top value 

"""

class MyStack(object):
    
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q1.append(x)


    def pop(self):
        """
        :rtype: int
        """
        
        for i in range(len(self.q1) - 1):
            self.q2.append(self.q1.pop(0))
            
        top_element = self.q1.pop(0)
        
        self.q1 , self.q2 = self.q2 , self.q1
        
        return top_element
        
        

    def top(self):
        """
        :rtype: int
        """
        for i in range(len(self.q1) - 1):
            self.q2.append(self.q1.pop(0))
            
        top_element = self.q1.pop(0)
        
        self.q2.append(top_element)
        
        self.q1 , self.q2 = self.q2 , self.q1
        
        return top_element
        
        

    def empty(self):
        """
        :rtype: bool
        """
        
        return (len(self.q1) == 0)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()