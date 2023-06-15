func getPermutation(n int, k int) string {
	fn := 1
	for i := 1; i <= n; i++ {
		fn *= i
	}

	used := make([]bool, n+1)
	res := make([]byte, 0, n)
	for i := 0; i < n; i++ {
		fn /= n - i
		count := 0
		for j := 1; j <= n; j++ {
			if used[j] {
				continue
			}
			count += fn
			if count >= k {
				res = append(res, byte(j)+'0')
				used[j] = true
				k -= count - fn
				break
			}
		}
	}
	return string(res)
}