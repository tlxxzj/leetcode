func spiralOrder(matrix [][]int) []int {
	m, n := len(matrix), len(matrix[0])
	res := make([]int, 0, m*n)

	x0, y0, x1, y1 := 0, 0, m-1, n-1
	x, y := 0, 0

	for len(res) < cap(res) {
		if x0 == x1 && y0 == y1 {
			res = append(res, matrix[x0][y0])
			break
		}
		for y < y1 && len(res) < cap(res) {
			res = append(res, matrix[x][y])
			y++
		}
		for x < x1 && len(res) < cap(res) {
			res = append(res, matrix[x][y])
			x++
		}
		for y > y0 && len(res) < cap(res) {
			res = append(res, matrix[x][y])
			y--
		}
		for x > x0 && len(res) < cap(res) {
			res = append(res, matrix[x][y])
			x--
		}
		x0, y0, x1, y1 = x0+1, y0+1, x1-1, y1-1
		x, y = x0, y0
	}
	return res
}
