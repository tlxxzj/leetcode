func findMinArrowShots(points [][]int) int {
	n := len(points)
	if n <= 1 {
		return n
	}
	sort.Slice(points, func(i, j int) bool {
		return points[i][1] < points[j][1]
	})

	res := 1
	right := points[0][1]
	for i := 1; i < n; i++ {
		if points[i][0] > right {
			res++
			right = points[i][1]
		} else if points[i][1] < right {
			right = points[i][1]
		}
	}
	return res
}