func knightDialer(n int) int {
	mod := 1000000007
	next := [][]int{
		{4, 6},
		{6, 8},
		{7, 9},
		{4, 8},
		{0, 3, 9},
		{},
		{0, 1, 7},
		{2, 6},
		{1, 3},
		{2, 4},
	}
	a := [10]int{1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
	b := [10]int{}
	for i := 1; i < n; i++ {
		for j := 0; j < 10; j++ {
			for _, k := range next[j] {
				b[k] += a[j]
				b[k] = b[k] % mod
			}
		}
		for j := 0; j < 10; j++ {
			a[j] = b[j]
			b[j] = 0
		}
	}
	res := 0
	for i := 0; i < 10; i++ {
		res = (res + a[i]) % mod
	}
	return res
}