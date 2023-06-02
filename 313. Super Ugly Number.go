func nthSuperUglyNumber(n int, primes []int) int {
	ugly := make([]int, n)
	ugly[0] = 1
	index := make([]int, len(primes))
	nums := make([]int, len(primes))
	min := 0
	for i := 1; i < n; i++ {
		min = math.MaxInt32
		for j := 0; j < len(primes); j++ {
			nums[j] = ugly[index[j]] * primes[j]
			if nums[j] < min {
				min = nums[j]
			}
		}
		ugly[i] = min
		for j := 0; j < len(primes); j++ {
			if nums[j] == min {
				index[j]++
			}
		}
	}
	return ugly[n-1]
}