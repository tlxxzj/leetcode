func isScramble(s1 string, s2 string) bool {
	m, n := len(s1), len(s2)
	if m != n {
		return false
	}

	dp := make([][][]bool, n)
	for i := 0; i < n; i++ {
		dp[i] = make([][]bool, n)
		for j := 0; j < n; j++ {
			dp[i][j] = make([]bool, n+1)
			if s1[i] == s2[j] {
				dp[i][j][1] = true
			}
		}
	}

	for k := 2; k <= n; k++ {
		for i := 0; i+k <= n; i++ {
			for j := 0; j+k <= n; j++ {
				for x := 1; x < k; x++ {
					if dp[i][j][x] && dp[i+x][j+x][k-x] {
						dp[i][j][k] = true
						break
					}
					if dp[i][j+k-x][x] && dp[i+x][j][k-x] {
						dp[i][j][k] = true
						break
					}
				}
			}
		}
	}
	return dp[0][0][n]
}
