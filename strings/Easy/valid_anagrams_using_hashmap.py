# Link:https://leetcode.com/problems/valid-anagram/
# Code:
# Anagrams are the words that have same alphabets but the order of alphabets is different
# For example 1:
# s="anagrams"
# t="nagaarsm"
# output:True
# because s and t are anagrams.
# example 2:
# s="a"
# t="ab"
# output:False
# because s and t are not anagrams.
#
# USING HASHMAP IN PYTHON
#
# There are two dictionaries hash_s and hash_t to store each alphabet with the number of occurences in s and t respectively.
# If the number of occurences of all the alphabets are same then it will return true and false otherwise.
class Solution(object):
    def isAnagram(self, s, t):
        hash_s = {}
        hash_t = {}
        flag = 0
        if (len(s) == len(t)):
            for i in range(len(s)):
                if s[i] in hash_s.keys():
                    hash_s.update({s[i]: hash_s[s[i]] + 1})
                else:
                    hash_s.update({s[i]: 1})

            for i in range(len(t)):
                if t[i] in hash_t.keys():
                    hash_t.update({t[i]: hash_t[t[i]] + 1})
                else:
                    hash_t.update({t[i]: 1})

            for i in range(len(t)):
                if (t[i] in s):
                    if (hash_t[t[i]] != hash_s[t[i]]):
                        flag = 1
                        break
                else:
                    flag = 1
            if (flag == 1):
                return False
            else:
                return True
        else:
            return False;

ob = Solution()
x= ob.isAnagram("ab","ab")
print(x)
# Running time complexity: O(n)