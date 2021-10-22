'''
Link - https://leetcode.com/problems/n-queens/ 

Difficulty - Hard

Approach:

We use 3 hashmaps safe_diag_down, safe_diag_up, safe_left to store and check valid positions while doing backtrack.

safe_diag_down - This is for checking if there is any Queen present in current diagonal ( top-down )

safe_diag_up - This is for checking if there is any Queen present in current diagonal ( down-top )

safe_left = This is for checking if the we have placed any Queen to the left of it or not

We're not using safe_right because we're going to column wise to the right and obviously they're not filled.

Time complexity is O(n!).
Space complexity is O(n), since the maximum recursion depth is n, also the length for all three hashmaps.
'''
class Solution(object):

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans = []
        safe_diag_down = {k: False for k in range(2 * n - 1)}
        safe_diag_up = {k: False for k in range(2 * n - 1)}
        safe_left = {k: False for k in range(n)}
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.main(0, n, board, ans, safe_diag_down, safe_diag_up, safe_left)

        return ans

    def main(self, col, n, board, ans, safe_diag_down, safe_diag_up, safe_left):
        if col == n:
            ans.append([''.join(board[i]) for i in range(n)])
            return
        for row in range(n):
            if not safe_diag_up[n-1+col-row] and not safe_left[row] and not safe_diag_down[col+row]:
                board[row][col] = 'Q'
                safe_diag_down[row + col] = True
                safe_diag_up[n-1 + col-row] = True
                safe_left[row] = True

                self.main(col + 1, n, board, ans, safe_diag_down, safe_diag_up, safe_left)

                board[row][col] = '.'
                safe_diag_down[row + col] = False
                safe_diag_up[n - 1 + col - row] = False
                safe_left[row] = False
                
