func findLongestWord(s string, dictionary []string) string {

	sort.Slice(dictionary, func(i, j int) bool {
		if len(dictionary[i]) == len(dictionary[j]) {
			return dictionary[i] < dictionary[j]
		}
		return len(dictionary[i]) > len(dictionary[j])
	})

	for _, word := range dictionary {
		i, j := 0, 0
		for i < len(s) && j < len(word) {
			if s[i] == word[j] {
				j++
			}
			i++
		}
		if j == len(word) {
			return word
		}
	}

	return ""
}
