func canCross(stones []int) bool {
	n := len(stones)
	if stones[1] != 1 {
		return false
	}
	if n == 2 {
		return true
	}
	dp := make([][]bool, n)
	for i := range dp {
		dp[i] = make([]bool, n+1)
	}
	dp[1][1] = true
	for i := 2; i < n; i++ {
		for j := i - 1; j > 0; j-- {
			k := stones[i] - stones[j]
			if k > j+1 {
				break
			}
			dp[i][k] = dp[j][k-1] || dp[j][k] || dp[j][k+1]
			if i == n-1 && dp[i][k] {
				return true
			}
		}
	}

	return false
}