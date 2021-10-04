class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        list_s = list(s)
        list_t = list(t)
        list_s.sort()
        list_t.sort()
        if(list_s == list_t):
          return True
        else:
          return False