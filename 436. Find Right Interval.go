func findRightInterval(intervals [][]int) []int {
	n := len(intervals)
	res := make([]int, n)
	for i := 0; i < n; i++ {
		res[i] = -1
	}

	index := make([]int, n)
	for i := 0; i < n; i++ {
		index[i] = i
	}
	less := func(i, j int) bool {
		return intervals[index[i]][0] < intervals[index[j]][0]
	}
	sort.Slice(index, less)

	for i := 0; i < n; i++ {
		l, r := 0, n
		for l < r {
			m := (l + r) / 2
			if intervals[index[m]][0] < intervals[i][1] {
				l = m + 1
			} else {
				r = m
			}
		}
		if l < n {
			res[i] = index[l]
		}
	}
	return res
}