func totalNQueens(n int) int {
	res := 0

	colVisited := make([]bool, n)
	leftVisited := make([]bool, 2*n-1)
	rightVisited := make([]bool, 2*n-1)

	var dfs func(row int)
	dfs = func(row int) {
		if row == n {
			res++
			return
		}

		for col := 0; col < n; col++ {
			if !colVisited[col] && !leftVisited[row+col] && !rightVisited[row-col+n-1] {
				colVisited[col] = true
				leftVisited[row+col] = true
				rightVisited[row-col+n-1] = true
				dfs(row + 1)
				colVisited[col] = false
				leftVisited[row+col] = false
				rightVisited[row-col+n-1] = false
			}
		}
	}

	dfs(0)
	return res
}