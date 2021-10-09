# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""
Problem statement:
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.


Solution:
Approach ==> Optimized Sliding Window

Working:

1. An empty dictionary (also called HashMap) is initialized, which will hold the visited characters of the string
   as keys and their (current index + 1) as values.
   For example, {key: value} <---> {'a': 1}

2. Two pointers i and j will handle the range of substrings which need to be traversed.

3. Initially, pointer i and j hold the starting index of the string.

4. j is incremented till a character is repeated.

5. When the character is repeated, i is set to new index. This new index i specifies the new range of the substrings that
   will be traversed further.

6. The length of the current substring (without repetitions) is compared with the previous max_length and updated if 
   it is greater.

7. This process from point 4 loops till all the characters are traversed.

"""


class Solution(object):
    def longestSubstringWithoutRepeatingCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """

        max_length = 0

        # visited: Dictionary to store the visited characters as keys and their (current index + 1) as values.
        visited = {}

        i = 0
        for j in range(len(s)):

            # Check if a character is repeated.
            if s[j] in visited.keys():
                # Update the range.
                i = max(visited[s[j]], i)

            # Compare the length of new substring (j - i + 1) with the old length and update it if greater than previous length.
            max_length = max(max_length, j - i + 1)

            # (current index + 1) for visited characters.
            visited[s[j]] = j + 1

        return max_length


# Time Complexity: O(n)


# Using Set : 


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Sliding window method 
        
        left_pointer = 0
        res = 0 
        char_set = set()
        
        for right_pointer in range(len(s)):
            
            while(s[right_pointer] in char_set):
                char_set.remove(s[left_pointer])
                left_pointer += 1 
                
            char_set.add(s[right_pointer]) 
            res = max(res , right_pointer - left_pointer + 1)
    
        return res


