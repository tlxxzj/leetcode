
func repeatedSubstringPattern(s string) bool {
	n := len(s)
	for m := n / 2; m > 0; m-- {
		if n%m == 0 {
			repeated := true
			for i := m; i < n && repeated; i += m {
				for j := 0; j < m && repeated; j++ {
					if s[j] != s[i+j] {
						repeated = false
					}
				}
			}
			if repeated {
				return true
			}
		}
	}
	return false
}
