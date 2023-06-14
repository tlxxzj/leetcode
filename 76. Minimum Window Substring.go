func minWindow(s string, t string) string {
	m, n := len(s), len(t)
	if m < n {
		return ""
	}

	res := ""
	nChar := 0
	chars := [128]int{}
	for i := 0; i < n; i++ {
		if chars[t[i]] == 0 {
			nChar++
		}
		chars[t[i]]++
	}

	l := 0
	subChars := [128]int{}
	for i := 0; i < m; i++ {
		if chars[s[i]] == 0 {
			continue
		}

		subChars[s[i]]++
		if subChars[s[i]] == chars[s[i]] {
			nChar--
		}

		for l <= i && (chars[s[l]] == 0 || subChars[s[l]] > chars[s[l]]) {
			subChars[s[l]]--
			l++
		}
		if nChar == 0 && (res == "" || i-l+1 < len(res)) {
			res = s[l : i+1]
		}
	}
	return res
}