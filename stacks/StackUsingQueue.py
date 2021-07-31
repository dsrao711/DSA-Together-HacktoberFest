#https://practice.geeksforgeeks.org/problems/stack-using-two-queues/1#


from queue import Queue

#User function Template for python3
'''
    :param x: value to be inserted
    :return: None

    queue_1 = [] # first queue
    queue_2 = [] # second queue
   '''
   
   
   
#Function to push an element into stack using two queues.
def push(x):
    
    # global declaration
    global queue_1
    global queue_2
    
    # code here
    queue_2.append(x)
    
    while(len(queue_1) != 0):
        
        queue_2.append(queue_1.pop(0))
        
        
    queue_1 , queue_2 = queue_2 , queue_1


#Function to pop an element from stack using two queues.     
def pop():
    
    # global declaration
    global queue_1
    global queue_2
    
    # code here
    
    if(len(queue_1) == 0):
        return -1
    else:
        return queue_1.pop(0)


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

queue_1 = [] # first queue
queue_2 = [] # second queue

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        i = 0
        while i<len(a):
            if a[i] == 1:
                push(a[i+1])
                i+=1
            else:
                print(pop(),end=" ")
            i+=1

        # clear both the queues
        queue_1 = []
        queue_2 = []
        print()
# } Driver Code Ends