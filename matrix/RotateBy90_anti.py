
#https://practice.geeksforgeeks.org/problems/rotate-by-90-degree0356/1/?company[]=Morgan%20Stanley&company[]=Morgan%20Stanley&page=1&query=company[]Morgan%20Stanleypage1company[]Morgan%20Stanley#

def transpose(matrix , n):
    for i in range(n):
        for j in range(n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
            
    
def reverse_columns(matrix , n):
    
    for i in range(n):
        j = 0
        k = n - 1
        while(j < k):
            temp = matrix[j][i]
            matrix[j][i] = matrix[k][i]
            matrix[k][i] = temp
            
            k -= 1
            j += 1
    
def rotate(matrix): 
    #code here
    n = len(matrix[0])
    transpose(matrix , n)
    reverse_columns(matrix , n)
    return matrix
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N=int(input())
        arr=[int(x) for x in input().split()]
        matrix=[]

        for i in range(0,N*N,N):
            matrix.append(arr[i:i+N])

        rotate(matrix)
        for i in range(N): 
            for j in range(N): 
                print(matrix[i][j], end =' ') 
            print() 
        

# } Driver Code Ends