# A Program to prints common element in all rows of matrix
# https://www.geeksforgeeks.org/common-elements-in-all-rows-of-a-given-matrix/
M = 4
N = 5


def printCommonElements(mat):

	mp = dict()
	
	for j in range(N):
		mp[mat[0][j]] = 1

	# traverse the matrix
	for i in range(1, M):
		for j in range(N):
			
			# If element is present in the map and is not duplicated in current row.
   
			if (mat[i][j] in mp.keys() and
							mp[mat[i][j]] == i):
								
			# we increment count of the element in map by 1
				mp[mat[i][j]] += 1

				# If this is last row
				if i == M - 1:
					print(mat[i][j], end = " ")
			
# Driver Code
mat = [[1, 2, 1, 4, 8],
	[3, 7, 8, 5, 1],
	[8, 7, 7, 3, 1],
	[8, 1, 2, 7, 9]]

printCommonElements(mat)

# This code is conteibuted
# by mohit kumar 29
