class Solution:

    def findMinDiff(self, A,N,M):

        # code here
        if(N == 0 or M == 0):
            return 0
        elif (N < M):
            return -1
        else:
            A.sort()
            # Window identified
            min_diff = A[N-1] - A[0]
            for i in range(0 , N - M + 1):
                min_diff = min(min_diff , A[i+M-1] - A[i])
            return min_diff


if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
