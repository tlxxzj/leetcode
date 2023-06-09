func rotate(matrix [][]int) {
	m := matrix
	n := len(m)
	for i := 0; i < n/2; i++ {
		for j := 0; j < n-i*2-1; j++ {
			a := &m[i][i+j]
			b := &m[i+j][n-i-1]
			c := &m[n-i-1][n-i-j-1]
			d := &m[n-i-j-1][i]
			*a, *b, *c, *d = *d, *a, *b, *c
		}
	}
}