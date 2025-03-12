func findKthNumber(n int, k int) int {
	getCount := func(m int) int {
		cnt := 0
		a := m
		b := m + 1
		for a <= n {
			cnt += min(n+1, b) - a
			a *= 10
			b *= 10
		}
		return cnt
	}

	res := 1
	k--
	for k > 0 {
		cnt := getCount(res)
		if cnt <= k {
			k -= cnt
			res++
		} else {
			res *= 10
			k--
		}
	}
	return res
}