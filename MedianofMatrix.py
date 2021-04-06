# Median in a row-wise sorted Matrix
#https://practice.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/

import statistics

class Solution:
    def median(self, matrix, r, c):
        #code here 
        list_matrix = []
        for i in range(0,r):
            for j in range(0 , c):
                list_matrix.append(matrix[i][j])
        
        list_matrix.sort()
        result = statistics.median(list_matrix)
        return result
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        line1 = [int(x) for x in input().strip().split()]       
        k = 0
        for i in range(r):
            for j in range (c):
                matrix[i][j]=line1[k]
                k+=1
        ans = ob.median(matrix, r, c);
        print(ans)
# } Driver Code Ends

