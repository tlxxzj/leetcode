func countBits(n int) []int {
	countBit := func(n int) int {
		res := 0
		for n > 0 {
			res++
			n &= n - 1
		}
		return res
	}
	res := make([]int, n+1)
	for i := 0; i <= n; i++ {
		res[i] = countBit(i)
	}
	return res
}