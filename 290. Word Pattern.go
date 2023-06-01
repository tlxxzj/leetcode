func wordPattern(pattern string, s string) bool {
	words := strings.Split(s, " ")
	if len(words) != len(pattern) {
		return false
	}

	m := make(map[byte]string)
	m2 := make(map[string]bool)
	for i := 0; i < len(pattern); i++ {
		if m[pattern[i]] == "" && !m2[words[i]] {
			m[pattern[i]] = words[i]
            m2[words[i]] = true
		} else if m[pattern[i]] != words[i] {
			return false
		}
	}
	return true
}