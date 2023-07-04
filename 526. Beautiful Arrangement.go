func countArrangement(n int) int {
	res := 0
	used := make([]bool, n+1)
	var dfs func(i int)
	dfs = func(i int) {
		if i == n+1 {
			res++
			return
		}
		for j := 1; j <= n; j++ {
			if !used[j] && (j%i == 0 || i%j == 0) {
				used[j] = true
				dfs(i + 1)
				used[j] = false
			}
		}
	}
	dfs(1)
	return res
}