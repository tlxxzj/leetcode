func constructArray(n int, k int) []int {
	res := make([]int, n)
	res[0] = 1
	j := 1
	for i := 0; i < k; i++ {
		res[i+1] = res[i] + (k-i)*j
		j = -j
	}
	for i := k+1;i<n;i++ {
		res[i] = i+1
	}
	return res
}