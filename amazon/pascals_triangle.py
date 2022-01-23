class Solution(object):
    def generate(self, numRows):
        
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        m = [[1]*i for i in range(1 , numRows  + 1 )]
        
        for i in range(numRows):
            for j in range(1 , len(m[i]) - 1):
                m[i][j] = m[i-1][j-1] + m[i-1][j]
        
        return m