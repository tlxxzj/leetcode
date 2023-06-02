func longestIncreasingPath(matrix [][]int) int {
	ret := 0
	m, n := len(matrix), len(matrix[0])
	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, n)
	}

	max := func(a, b int) int {
		if a < b {
			return b
		}
		return a
	}
	var dfs func(i, j, k, num int)
	dfs = func(i, j, k, num int) {
		if i < 0 || i >= m || j < 0 || j >= n || matrix[i][j] <= num || k <= dp[i][j] {
			return
		}
		ret = max(ret, k)
		dp[i][j] = k

		dfs(i+1, j, k+1, matrix[i][j])
		dfs(i-1, j, k+1, matrix[i][j])
		dfs(i, j+1, k+1, matrix[i][j])
		dfs(i, j-1, k+1, matrix[i][j])
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			dfs(i, j, 1, -1)
		}
	}
	return ret
}