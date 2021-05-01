# A hashing based Python program to find if there are
# four elements with given summ.

# The function finds four elements with given summ X

def findFourElements(arr, n, X):

	# Store summs of all pairs in a hash table
	mp = {}
	for i in range(n - 1):
		for j in range(i + 1, n):
			mp[arr[i] + arr[j]] = [i, j]

	# Traverse through all pairs and search
	# for X - (current pair summ).
	for i in range(n - 1):
		for j in range(i + 1, n):
			summ = arr[i] + arr[j]

			# If X - summ is present in hash table,
			if (X - summ) in mp:

				# Making sure that all elements are
				# distinct array elements and an element
				# is not considered more than once.
				p = mp[X - summ]
				if (p[0] != i and p[0] != j and p[1] != i and p[1] != j):
					print(arr[i], ", ", arr[j], ", ",
						arr[p[0]], ", ", arr[p[1]], sep="")
					return


# Driver code
arr = [10, 20, 30, 40, 1, 2]
n = len(arr)
X = 91

# Function call
findFourElements(arr, n, X)

