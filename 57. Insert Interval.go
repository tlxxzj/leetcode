func insert(intervals [][]int, newInterval []int) [][]int {
	min := func(a, b int) int {
		if a < b {
			return a
		}
		return b
	}

	max := func(a, b int) int {
		if a < b {
			return b
		}
		return a
	}

	n := len(intervals)
	res := make([][]int, 0, n+1)
	for i := 0; i < n; i++ {
		if newInterval[1] < intervals[i][0] {
			res = append(res, newInterval)
			res = append(res, intervals[i:]...)
			return res
		}

		if newInterval[0] > intervals[i][1] {
			res = append(res, intervals[i])
			continue
		}

		newInterval[0] = min(newInterval[0], intervals[i][0])
		newInterval[1] = max(newInterval[1], intervals[i][1])
	}

	res = append(res, newInterval)
	return res
}
