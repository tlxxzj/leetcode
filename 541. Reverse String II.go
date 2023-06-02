func reverseStr(s string, k int) string {
	n := len(s)
	s2 := make([]byte, n)
	for i := 0; i < n; i += 2 * k {
        z := i+k-1
        if z > n - 1{
            z = n -1 
        }
		for j := 0; j < k && i+j < n; j++ {
			s2[i+j] = s[z-j]
		}
		for j := 0; j < k && i+j+k < n; j++ {
			s2[i+j+k] = s[i+j+k]
		}
	}
	return string(s2)
}