# A O(n) solution that uses
# table fact[] to calculate
# the Permutation Coefficient

# Returns value of Permutation
# Coefficient P(n, k)
def permutationCoeff(n, k):
	fact = [0 for i in range(n + 1)]

	# base case
	fact[0] = 1

	# Calculate value
	# factorials up to n
	for i in range(1, n + 1):
		fact[i] = i * fact[i - 1]

	# P(n, k) = n!/(n-k)!
	return int(fact[n] / fact[n - k])

# Driver Code
n = 10
k = 2
print("Value of P(", n, ", ", k, ") is ",
		permutationCoeff(n, k), sep = "")

# This code is contributed
# by Soumen Ghosh
