class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        
        for i in range(0 , n + 1):
          binary = format(i , "b")
          ones = str(binary).count('1')
          ans.append(ones)
          
        return ans
          