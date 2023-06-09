func convert(s string, numRows int) string {
	n := len(s)
	if n <= numRows || numRows == 1 {
		return s
	}
	m := numRows*2 - 2
	res := make([]byte, 0, n)
	for i := 0; i < numRows; i++ {
		for j := i; j < n; j += m {
			res = append(res, s[j])
			if i != 0 && i != numRows-1 && j+m-2*i < n {
				res = append(res, s[j+m-2*i])
			}
		}
	}
	return string(res)
}