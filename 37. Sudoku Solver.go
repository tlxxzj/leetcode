func solveSudoku(board [][]byte) {
	rows := [10][10]bool{}
	cols := [10][10]bool{}
	grids := [3][3][10]bool{}

	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			k := board[i][j] - '0'
			if k > 0 && k <= 9 {
				rows[i][k] = true
				cols[j][k] = true
				grids[i/3][j/3][k] = true
			}
		}
	}

	var dfs func(int, int) bool
	dfs = func(i, j int) bool {
		if i == 9 {
			return true
		}
		if board[i][j] != '.' {
			return dfs(i+(j+1)/9, (j+1)%9)
		}

		for k := 1; k <= 9; k++ {
			if rows[i][k] || cols[j][k] || grids[i/3][j/3][k] {
				continue
			}
			board[i][j] = byte(k + '0')
			rows[i][k] = true
			cols[j][k] = true
			grids[i/3][j/3][k] = true
			if dfs(i+(j+1)/9, (j+1)%9) {
				return true
			}
			board[i][j] = '.'
			rows[i][k] = false
			cols[j][k] = false
			grids[i/3][j/3][k] = false
		}
		return false
	}
	dfs(0, 0)
}