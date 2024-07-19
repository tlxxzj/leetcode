
func findLUSlength(strs []string) int {
	slices.SortFunc(strs, func(a, b string) int {
		return -(len(a) - len(b))
	})

	isSub := func(a, b string) bool {
		if len(a) > len(b) {
			return false
		}
		i, j := 0, 0
		for i < len(a) && j < len(b) {
			if a[i] == b[j] {
				i++
			}
			j++
		}
		return i == len(a)
	}

	for i := 0; i < len(strs); i++ {
		hasSub := false
		for j := 0; j < len(strs) && len(strs[j]) >= len(strs[i]); j++ {
			if i == j {
				continue
			}

			if isSub(strs[i], strs[j]) {
				hasSub = true
				break
			}
		}
		if !hasSub {
			return len(strs[i])
		}
	}
	return -1
}
