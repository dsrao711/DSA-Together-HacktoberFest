#include<bits/stdc++.h>
using namespace std;

// Dynamic Programming C implementation of LCS problem

int max(int a, int b);

// Returns length of LCS for X[0..m-1], Y[0..n-1]
int lcs( string X, string Y, int m, int n )
{
  int dp[m+1][n+1];
  int i, j;

  // Following steps build DP[m+1][n+1] in bottom up fashion. Note
 // that DP[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]

  for (i=0; i<=m; i++)
  {
  	for (j=0; j<=n; j++)
  	{
  	if (i == 0 || j == 0)
  		dp[i][j] = 0;

  	else if (X[i-1] == Y[j-1])
  		dp[i][j] = dp[i-1][j-1] + 1;

  	else
  		dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
  	}
  }

  // DP[m][n] contains length of LCS for X[0..n-1] and Y[0..m-1]

  return dp[m][n];
}



int max(int a, int b)
{
	return (a > b)? a : b;
}

int main()
{
  string X = "AGGTAB";
  string Y = "GXTXAYB";

  int m = X.size();
  int n = Y.size();

  cout<<"Length of LCS is "<<lcs( X, Y, m, n );

  return 0;
}
