class Solution:
    def find(self, m, n, visited, ans, s, i, j):
        if i == n-1 and j == n-1:
            ans.append(s)
            return
        visited[i][j] = 1

        # Go Down and marking the path as visited
        if i < n-1 and visited[i+1][j] == 0 and m[i+1][j] == 1:
            visited[i+1][j] = 1
            self.find(m, n, visited, ans, s+'D', i+1, j)
            visited[i+1][j] = 0

        # Go Right and marking the path as visited
        if j < n-1 and visited[i][j+1] == 0 and m[i][j+1] == 1:
            visited[i][j+1] = 1
            self.find(m, n, visited, ans, s+'R', i, j+1)
            visited[i][j+1] = 0

        # Go Up and marking the path as visited
        if i > 0 and visited[i-1][j] == 0 and m[i-1][j] == 1:
            visited[i-1][j] = 1
            self.find(m, n, visited, ans, s+'U', i-1, j)
            visited[i-1][j] = 0

        # Go Left and marking the path as visited
        if j > 0 and visited[i][j-1] == 0 and m[i][j-1] == 1:
            visited[i][j-1] = 1
            self.find(m, n, visited, ans, s+'L', i, j-1)
            visited[i][j-1] = 0
        visited[i][j] = 0
        return False

    def findPath(self, m, n):
        visited = [[0 for i in range(n)] for i in range(n)]
        if m[n-1][n-1] == 0:
            return []
        if m[0][0] == 0:
            return []
        ans = []
        self.find(m, n, visited, ans, '', 0, 0)
        if ans == []:
            return []
        return sorted(ans)
