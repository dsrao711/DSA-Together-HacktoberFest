# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        output = False
        rows = len(matrix)
        columns = len(matrix[0])

        if(rows == 1 and columns == 1):
            # For 1x1 matrix like : matrix = [[1]] 
            if(target == matrix[0][0]):
                return True
            else:
                return False

        result = False
        j = len(matrix[0]) - 1
        
        for i in range(0 , rows):

            if(target == matrix[i][j]):
                result =  True
            elif (target <= matrix[i][j]):
                result = self.search(matrix[i] , target)
                break

        return result

# Implementing Binary Search 

     def search(self, arr, target):
            beg_index = 0
        end_index = len(arr) - 1
        while beg_index <= end_index :
            mid = (beg_index + end_index ) // 2
            if arr[mid] == target:
                return True
            elif target < arr[mid]:
                end_index = mid - 1
            else:
                beg_index = mid + 1
        return False


       