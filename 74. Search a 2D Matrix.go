
func searchMatrix(matrix [][]int, target int) bool {
	m, n := len(matrix), len(matrix[0])
	l, r := 0, m
	for l < r {
		mid := (l + r) / 2
		if matrix[mid][n-1] == target {
			return true
		}
		if matrix[mid][n-1] < target {
			l = mid + 1
		} else {
			r = mid
		}
	}
	if l == m {
		return false
	}
	row := l
	l, r = 0, n
	for l < r {
		mid := (l + r) / 2
		if matrix[row][mid] == target {
			return true
		}
		if matrix[row][mid] < target {
			l = mid + 1
		} else {
			r = mid
		}
	}

	return false
}
