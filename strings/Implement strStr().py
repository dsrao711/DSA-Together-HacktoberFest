# Link to problem : https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        op = haystack.find(needle)
        return op