func exist(board [][]byte, word string) bool {
	m, n := len(board), len(board[0])
	visited := make([]int, m*n)

	var existHelper func(i, j, k int) bool
	existHelper = func(i, j, k int) bool {
		if i < 0 || i >= m || j < 0 || j >= n || visited[i*n+j] == 1 || board[i][j] != word[k] {
			return false
		}

		if k == len(word)-1 {
			return true
		}

		visited[i*n+j] = 1
		if existHelper(i-1, j, k+1) || existHelper(i+1, j, k+1) || existHelper(i, j-1, k+1) || existHelper(i, j+1, k+1) {
			return true
		} else {
			visited[i*n+j] = 0
			return false
		}
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if board[i][j] == word[0] && existHelper(i, j, 0) {
				return true
			}
		}
	}
	return false
}
