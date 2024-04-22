func longestWord(words []string) string {
	set := make(map[string]bool)
	for _, word := range words {
		set[word] = true
	}
	sort.Slice(words, func(a, b int) bool {
		if len(words[a]) == len(words[b]) {
			return words[a] < words[b]
		}
		return len(words[a]) > len(words[b])
	})

	res := ""
	for _, word := range words {
		valid := true
		for i := 1; i < len(word); i++ {
			if !set[word[:i]] {
				valid = false
				break
			}
		}
		if valid {
			res = word
			break
		}
	}
	return res
}
