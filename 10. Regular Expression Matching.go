func isMatch(s string, p string) bool {
	m, n := len(s), len(p)
	f := make([][]bool, m+1)
	for i := 0; i < m+1; i++ {
		f[i] = make([]bool, n+1)
	}
	f[0][0] = true

	for j := 0; j < n; j++ {
		if p[j] == '*' {
			f[0][j+1] = f[0][j-1]
		}
		for i := 0; i < m; i++ {
			if s[i] == p[j] || p[j] == '.' {
				f[i+1][j+1] = f[i][j]
			} else if p[j] == '*' {
				if s[i] == p[j-1] || p[j-1] == '.' {
					f[i+1][j+1] = f[i+1][j] || f[i][j+1]
				}
				f[i+1][j+1] = f[i+1][j+1] || f[i+1][j-1]
			}
		}
	}
	return f[m][n]
}