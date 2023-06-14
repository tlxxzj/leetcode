func maximalSquare(matrix [][]byte) int {
	res := 0
	m, n := len(matrix), len(matrix[0])
	dp := make([][]int, m+1)
	for i := 0; i < m+1; i++ {
		dp[i] = make([]int, n+1)
	}

	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			// sum of left, top,
			dp[i][j] = int(matrix[i-1][j-1]-'0') + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
		}
	}
	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			for k := 0; k+i <= m && k+j <= n; k++ {
				sum := dp[i+k][j+k] - dp[i-1][j+k] - dp[i+k][j-1] + dp[i-1][j-1]
				if sum == (k+1)*(k+1) && sum > res {
					res = sum
				}
			}
		}
	}
	return res
}
