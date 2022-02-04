# https://leetcode.com/problems/excel-sheet-column-number/

class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        
        n = len(columnTitle)
        res = 0
        
        if(n == 1):
            return ord(columnTitle.lower()) - 96
        
        for i in range(n-1 , -1 , -1 ):
            print(i)
            res += (ord(columnTitle[i].lower()) - 96) * 26**(n-i-1)
            print(res)
                        
        return res
                
            
            