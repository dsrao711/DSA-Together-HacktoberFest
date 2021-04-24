# Rotate the given matrix by 90 degree
# https://www.geeksforgeeks.org/rotate-a-matrix-by-90-degree-in-clockwise-direction-without-using-any-extra-space/

def rotateBy90(arr) :
    N = 4
    for j in range(N) :
        for i in range(N-1 , -1 , -1):
            print(arr[i][j] , end = " ")
        print()
    
arr = [ [ 1 , 23, 4, 4,] ,
        [2 , 5 , 5, 7] ,
        [2 , 4 , 9 , 0], 
        [2 , 3 , 8 , 92]]

rotateBy90(arr)