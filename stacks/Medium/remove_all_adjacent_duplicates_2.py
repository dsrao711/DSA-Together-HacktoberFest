# Link : https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/submissions/

"""
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.


Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"


"""


"""

Approach : 

Create a stack which stores the each char of the string with the count 
The moment , count is equal to K , the entry will be deleted from the stack 


"""

class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        # Eg : stack = [['d' , 1] , ['e' , 3]]
        
        stack = []
        
        for c in s : 
            # Check if stack is not empty and top element is equal to the char
            if stack and stack[-1][0] == c :
                # If yes , increase the counter
                stack[-1][1] += 1
                # If the count of this char is equal to k , remove it 
                if(stack[-1][1] >= k):
                    stack.pop()
            # Else , add the first occurence
            else:
                stack.append([c , 1])
                
        result = ''
        
        # Return the output as string with the remaining charachters
        for arr in stack:
            result += (arr[0]*arr[1])
            
        
        return result 