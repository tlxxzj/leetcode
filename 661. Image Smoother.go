func imageSmoother(img [][]int) [][]int {
	m, n := len(img), len(img[0])
	res := make([][]int, m)
	for i := range res {
		res[i] = make([]int, n)
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			count := 0
			for x := i - 1; x <= i+1; x++ {
				for y := j - 1; y <= j+1; y++ {
					if x >= 0 && x < m && y >= 0 && y < n {
						res[i][j] += img[x][y]
						count++
					}
				}
			}
			res[i][j] /= count
		}
	}
	return res
}
