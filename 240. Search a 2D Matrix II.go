func searchMatrix(matrix [][]int, target int) bool {
	m, n := len(matrix), len(matrix[0])
	x1, y1, x2, y2 := 0, 0, m-1, n-1
	for x1 <= x2 && y1 <= y2 {
		if matrix[x1][y1] == target || matrix[x2][y2] == target || matrix[x1][y2] == target || matrix[x2][y1] == target {
			return true
		}
		if matrix[x1][y2] < target {
			x1++
		} else {
			y2--
		}
		if matrix[x2][y1] < target {
			y1++
		} else {
			x2--
		}
	}
	return false
}
