func findMaxForm(strs []string, m int, n int) int {
	max := func(x, y int) int {
		if x < y {
			return y
		}
		return x
	}

	k := len(strs)
	dp := make([][]int, m+1)
	for i := 0; i < m+1; i++ {
		dp[i] = make([]int, n+1)
	}

	for i := 0; i < k; i++ {
		zero := 0
		one := 0
		for _, v := range strs[i] {
			if v == '0' {
				zero++
			} else {
				one++
			}
		}
		for x := m; x >= 0; x-- {
			for y := n; y >= 0; y-- {
				if x >= zero && y >= one {
					dp[x][y] = max(dp[x][y], dp[x-zero][y-one]+1)
				}
				if x > 0 {
					dp[x][y] = max(dp[x][y], dp[x-1][y])
				}
				if y > 0 {
					dp[x][y] = max(dp[x][y], dp[x][y-1])
				}
			}
		}
	}
	return dp[m][n]
}
