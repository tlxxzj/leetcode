func splitArray(nums []int, k int) int {
	n := len(nums)
	sum := make([]int, n+1)
	for i := 0; i < n; i++ {
		sum[i+1] = sum[i] + nums[i]
	}

	check := func(x int) bool {
		cnt := 1
		startIndex := 0
		for i := 1; i <= n; i++ {
			if nums[i-1] > x {
				return false
			}
			if sum[i]-sum[startIndex] > x {
				cnt++
				startIndex = i - 1
			}
		}
		return cnt <= k
	}

	l, r := sum[n]/k, sum[n]
	for l < r {
		m := (l + r) / 2
		if !check(m) {
			l = m + 1
		} else {
			r = m
		}
	}
	return l
}