from collections import deque
def minStepToReachTarget(self, KnightPos, TargetPos, N):
    # Code here
    # Get knight pos and target pos cords

    x1 = KnightPos[0]
    y1 = KnightPos[1]
    x2 = TargetPos[0]
    y2 = TargetPos[1]

    if(x1 == x2 and y1 == y2):
        return 0

    a = [[0]*N]*N
    q = deque()

    # Make zero based indexing
    q.append([x1-1, y1-1])

    # Bfs
    while(q):

        curr = q.popleft()
        print(curr)
        i = curr[0]
        j = curr[1]

        if(i-2 >= 0 and j+1 >= 0 and i-2 < N and j+1 < N and a[i-2][j+1] == 0):
            a[i-2][j+1] = a[i][j] + 1
            q.append([i-2, j+1])

        if(i-2 >= 0 and j-1 >= 0 and i-2 < N and j-1 < N and a[i-2][j-1] == 0):
            a[i-2][j-1] = a[i][j] + 1
            q.append([i-2, j-1])

        if(i+2 >= 0 and j-1 >= 0 and i+2 < N and j-1 < N and a[i+2][j-1] == 0):
            a[i+2][j-1] = a[i][j] + 1
            q.append([i+2, j-1])

        if(i+2 >= 0 and j+1 >= 0 and i+2 < N and j+1 < N and a[i+2][j+1] == 0):
            a[i+2][j+1] = a[i][j] + 1
            q.append([i+2, j+1])

        if(i-1 >= 0 and j-2 >= 0 and i-1 < N and j-2 < N and a[i-1][j-2] == 0):
            a[i-1][j-2] = a[i][j] + 1
            q.append([i-1, j-2])

        if(i+1 >= 0 and j-2 >= 0 and i+1 < N and j-2 < N and a[i+1][j-2] == 0):
            a[i+1][j-2] = a[i][j] + 1
            q.append([i+1, j-2])

        if(i-1 >= 0 and j+2 >= 0 and i-1 < N and j+2 < N and a[i-1][j+2] == 0):
            a[i-1][j+2] = a[i][j] + 1
            q.append([i-1, j+2])

        if(i+1 >= 0 and j+2 >= 0 and i+1 < N and j+2 < N and a[i+1][j+2] == 0):
            a[i+1][j+2] = a[i][j] + 1
            q.append([i+1, j+2])

    return a[x2-1][y2-1]
