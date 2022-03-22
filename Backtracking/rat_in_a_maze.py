MAX = 5
class Solution:
    
    def isSafe(self ,row, col, m, n,
           visited):

        if (row == -1 or row == n or 
            col == -1 or col == n or 
            visited[row][col] or m[row][col] == 0):
            return False
    
        return True

    def printPathUtil(self , row, col, m, n, path, possiblePaths , visited):
    
        # This will check the initial point
        # (i.e. (0, 0)) to start the paths.
        if (row == -1 or row == n or 
            col == -1 or col == n or
            visited[row][col] or m[row][col] == 0):
            return
    
        # If reach the last cell (n-1, n-1)
        # then store the path and return
        if (row == n - 1 and col == n - 1):
            possiblePaths.append(path)
            return
    
        # Mark the cell as visited
        visited[row][col] = True
    
        # Try for all the 4 directions (down, left,
        # right, up) in the given order to get the
        # paths in lexicographical order
    
        # Check if downward move is valid
        if (self.isSafe(row + 1, col, m, n, visited)):
            path += 'D'
            self.printPathUtil(row + 1, col, m, n, 
                          path, possiblePaths, visited)
            path = path[:-1]
    
        # Check if the left move is valid
        if (self.isSafe(row, col - 1, m, n, visited)):
            path += 'L'
            self.printPathUtil(row, col - 1, m, n, 
                          path, possiblePaths, visited)
            path = path[:-1]
    
        # Check if the right move is valid
        if (self.isSafe(row, col + 1, m, n, visited)):
            path += 'R'
            self.printPathUtil(row, col + 1, m, n,
                          path, possiblePaths, visited)
            path = path[:-1]
    
        # Check if the upper move is valid
        if (self.isSafe(row - 1, col, m, n, visited)):
            path += 'U'
            self.printPathUtil(row - 1, col, m, n,
                          path, possiblePaths, visited)
            path = path[:-1]
    
        # Mark the cell as unvisited for
        # other possible paths
        visited[row][col] = False
        
    def findPath(self, m, n):
        # code here
        possiblePaths = []
        path = ""
        visited = [[False for _ in range(MAX)]
                          for _ in range(n)]
                          
       
        self.printPathUtil(0, 0, m, n, path, 
                      possiblePaths, visited)
    
        return possiblePaths


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
