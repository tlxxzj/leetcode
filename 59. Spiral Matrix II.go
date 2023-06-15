func generateMatrix(n int) [][]int {
	matrix := make([][]int, n)
	for i := 0; i < n; i++ {
		matrix[i] = make([]int, n)
	}
	up, down, left, right := 0, n-1, 0, n-1
	num := 1
	for {
		for i := left; i <= right; i++ {
			matrix[up][i] = num
			num++
		}
		up++
		if up > down {
			break
		}
		for i := up; i <= down; i++ {
			matrix[i][right] = num
			num++
		}
		right--
		if left > right {
			break
		}
		for i := right; i >= left; i-- {
			matrix[down][i] = num
			num++
		}
		down--
		if up > down {
			break
		}
		for i := down; i >= up; i-- {
			matrix[i][left] = num
			num++
		}
		left++
		if left > right {
			break
		}
	}
	return matrix
}