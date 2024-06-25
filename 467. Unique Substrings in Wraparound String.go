func findSubstringInWraproundString(s string) int {
	counts := make([]int, 26)
	preV := -1
	preLen := 0
	for _, c := range s {
		v := int(c - 'a')
		if (preV != -1 && v == preV+1) || (preV == 25 && v == 0) {
			preLen++
		} else {
			preLen = 1
		}
        preV = v
		counts[v] = max(counts[v], preLen)
	}
	sum := 0
	for _, c := range counts {
		sum += c
	}
	return sum
}
