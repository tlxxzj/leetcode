func largestDivisibleSubset(nums []int) []int {
	n := len(nums)
	sort.Ints(nums)

	maxi, maxl := 0, 0
	dp := make([]int, n)
	pre := make([]int, n)

	for i := 0; i < n; i++ {
		if dp[i] == 0 {
			dp[i] = 1
			pre[i] = -1
		}
		for j := i + 1; j < n; j++ {
			if nums[j]%nums[i] == 0 && dp[j] < dp[i]+1 {
				dp[j] = dp[i] + 1
				pre[j] = i
			}
		}
		if dp[i] > maxl {
			maxl = dp[i]
			maxi = i
		}
	}

	res := make([]int, 0, maxl)
	for i := maxi; i >= 0; i = pre[i] {
		res = append(res, nums[i])
	}

	return res
}
