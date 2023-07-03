func eraseOverlapIntervals(intervals [][]int) int {
	n := len(intervals)
	if n <= 1 {
		return 0
	}

	less := func(i, j int) bool {
		if intervals[i][0] == intervals[j][0] {
			return intervals[i][1] < intervals[j][1]
		}
		return intervals[i][0] < intervals[j][0]
	}
	sort.Slice(intervals, less)

	res := 0
	right := intervals[0][1]
	for i := 1; i < n; i++ {
		if intervals[i][0] < right {
			res++
			if intervals[i][1] < right {
				right = intervals[i][1]
			}
		} else {
			right = intervals[i][1]
		}
	}

	return res
}