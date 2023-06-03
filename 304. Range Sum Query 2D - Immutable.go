type NumMatrix struct {
	row int
	col int
	sum [][]int
}

func Constructor(matrix [][]int) NumMatrix {
	numMatrix := NumMatrix{
		row: len(matrix),
		col: len(matrix[0]),
	}
	numMatrix.sum = make([][]int, numMatrix.row+1)
	for i := 0; i < numMatrix.row+1; i++ {
		numMatrix.sum[i] = make([]int, numMatrix.col+1)
	}

	for i := 1; i <= numMatrix.row; i++ {
		for j := 1; j <= numMatrix.col; j++ {
			numMatrix.sum[i][j] = numMatrix.sum[i-1][j] + numMatrix.sum[i][j-1] - numMatrix.sum[i-1][j-1] + matrix[i-1][j-1]
		}
	}

	return numMatrix
}

func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
	return this.sum[row2+1][col2+1] - this.sum[row1][col2+1] - this.sum[row2+1][col1] + this.sum[row1][col1]
}
