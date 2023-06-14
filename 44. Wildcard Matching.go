func isMatch(s string, p string) bool {
	m, n := len(s), len(p)
	dp := make([][]bool, m+1)
	for i := range dp {
		dp[i] = make([]bool, n+1)
	}
	dp[0][0] = true

	for j := 0; j < n; j++ {
		if p[j] == '*' {
			dp[0][j+1] = dp[0][j]
		}
		for i := 0; i < m; i++ {
			if s[i] == p[j] || p[j] == '?' {
				dp[i+1][j+1] = dp[i][j]
			} else if p[j] == '*' {
				dp[i+1][j+1] = dp[i][j] || dp[i+1][j] || dp[i][j+1]
			}
		}
	}
	return dp[m][n]
}