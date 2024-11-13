func cherryPickup(grid [][]int) int {
	n := len(grid)
	dp := make([][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]int, n)
		for j := 0; j < n; j++ {
			dp[i][j] = math.MinInt
		}
	}
	dp[0][0] = grid[0][0]
	for k := 1; k < 2*n-1; k++ {
		for x1 := min(k, n-1); x1 >= max(k-n+1, 0); x1-- {
			for x2 := min(k, n-1); x2 >= x1; x2-- {
				y1 := k - x1
				y2 := k - x2
				if grid[x1][y1] == -1 || grid[x2][y2] == -1 {
					dp[x1][x2] = math.MinInt
					continue
				}

				v := dp[x1][x2]
				if x1 > 0 {
					v = max(v, dp[x1-1][x2])
				}
				if x2 > 0 {
					v = max(v, dp[x1][x2-1])
				}
				if x1 > 0 && x2 > 0 {
					v = max(v, dp[x1-1][x2-1])
				}
				v += grid[x1][y1]
				if x1 != x2 {
					v += grid[x2][y2]
				}
				dp[x1][x2] = v
			}
		}
	}
	return max(dp[n-1][n-1], 0)
}
