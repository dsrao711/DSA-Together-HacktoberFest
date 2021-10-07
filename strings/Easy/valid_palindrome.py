# Problem Title: Valid Palindrome
# Link: https://leetcode.com/problems/valid-palindrome/
"""
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example 1:

    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

Constraints:

    1 <= s.length <= 2 * 10^5
    s consists only of printable ASCII characters.

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
    	start, end = 0, len(s) - 1
    	while start < end:
    		startChar, endChar = s[start].lower(), s[end].lower()
    		if startChar.isalnum() and endChar.isalnum():
    			if startChar != endChar: return False
    			else:
    				start, end = start + 1, end - 1
    				continue
    		start, end = start + (not startChar.isalnum()), end - (not endChar.isalnum())
    	return True

# main block
if __name__ == "__main__":
    s = input()   # takes the input
    result = Solution().isPalindrome(s)
    print(result)