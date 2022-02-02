
#  https://practice.geeksforgeeks.org/problems/next-larger-element-1587115620/1/#
# ref : Pepcoding - next greater ele on the right

class Solution:
    def nextLargerElement(self,nums,n):
        #code here

        stack = []
        stack.append(nums[-1])
    
        op = [0]*n
        op[-1] = -1
                
        for i in range(n-2 , -1 , -1):
            while(len(stack) != 0 and stack[-1] <= nums[i]):
                #Pop till max found
                stack.pop()
            if(len(stack) == 0):
                # -1 if stack empty
                    op[i] = -1
            else:
                peek = stack[-1]
                op[i] = peek
                stack.append(peek)
                
            stack.append(nums[i]) 
           
        return op

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())

        a = list(map(int,input().strip().split()))
        obj = Solution()
        res = obj.nextLargerElement(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()
