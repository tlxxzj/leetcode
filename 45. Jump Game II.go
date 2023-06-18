
func jump(nums []int) int {
	min := func(a, b int) int {
		if a < b {
			return a
		}
		return b
	}

	n := len(nums)

	dp := make([]int, n)
	for i := 1; i < n; i++ {
		dp[i] = n
	}

	for i := 0; i < n; i++ {
		for j := min(i+nums[i], n-1); j > i; j-- {
			if dp[j] > dp[i]+1 {
				dp[j] = dp[i] + 1
			} else {
				break
			}
		}
	}
	return dp[n-1]
}
