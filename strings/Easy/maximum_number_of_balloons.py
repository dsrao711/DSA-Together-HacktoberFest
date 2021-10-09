# Problem Title: Maximum Number of Balloons
# Link: https://leetcode.com/problems/maximum-number-of-balloons/
"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:

    Input: text = "nlaebolko"
    Output: 1

Example 2:

    Input: text = "loonbalxballpoon"
    Output: 2

Example 3:

    Input: text = "leetcode"
    Output: 0


Constraints:

    1 <= text.length <= 104
    text consists of lower case English letters only.

"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if len(text) < len("balloon"):
            return 0
        wordChars = {'b':0,'a':0,'l':0,'o':0,'n':0}
        for c in text:
            if c in wordChars:
                wordChars[c] += 1
        
        
        res = float("inf")
        wordChars['l'] = wordChars['l'] // 2
        wordChars['o'] = wordChars['o'] // 2
        for index, key in enumerate(wordChars):
            res = min(res, wordChars[key])
        
        return res

# main block
if __name__ == "__main__":
    text = input()   # takes the input
    result = Solution().maxNumberOfBalloons(text)
    print(result)
