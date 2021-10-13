def lcs(s1 , s2):
    m, n = len(s1), len(s2)
    prev, cur = [0]*(n+1), [0]*(n+1)
    for i in range(1, m+1):
    	for j in range(1, n+1):
    		if s1[i-1] == s2[j-1]:
    			cur[j] = 1 + prev[j-1]
    		else:
    			if cur[j-1] > prev[j]:
    				cur[j] = cur[j-1]
    			else:
    				cur[j] = prev[j]
    	cur, prev = prev, cur
    return prev[n]

#end of function lcs


# Driver program to test the above function
s1 = "AGGTAB"
s2 = "GXTXAYB"
print("Length of LCS is ", lcs(s1, s2))
# BY PRASHANT SHEKHAR MISHRA
