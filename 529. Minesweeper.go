func updateBoard(board [][]byte, click []int) [][]byte {
	m, n := len(board), len(board[0])

	dx := []int{-1, -1, -1, 0, 0, 1, 1, 1}
	dy := []int{-1, 0, 1, -1, 1, -1, 0, 1}

	adjacentMines := func(x, y int) int {
		count := 0
		for i := 0; i < 8; i++ {
			nx, ny := x+dx[i], y+dy[i]
			if nx < 0 || nx >= m || ny < 0 || ny >= n {
				continue
			}
			if board[nx][ny] == 'M' {
				count++
			}
		}
		return count
	}

	var reveal func(x, y int)
	reveal = func(x, y int) {
		if x < 0 || x >= m || y < 0 || y >= n {
			return
		}

		if board[x][y] == 'M' {
			board[x][y] = 'X'
			return
		}

		mines := adjacentMines(x, y)
		if mines > 0 {
			board[x][y] = byte('0' + mines)
			return
		}

		board[x][y] = 'B'
		for i := 0; i < 8; i++ {
			nx, ny := x+dx[i], y+dy[i]
			if nx < 0 || nx >= m || ny < 0 || ny >= n {
				continue
			}
			if board[nx][ny] == 'E' {
				reveal(nx, ny)
			}
		}
	}

	reveal(click[0], click[1])
	return board
}
