func findAllConcatenatedWordsInADict(words []string) []string {
	wordMap := make(map[string]bool)
	for _, word := range words {
		wordMap[word] = true
	}

	var result []string
	var visited [32]bool

	var dfs func(word string, start, wordN int) bool
	dfs = func(word string, start, wordN int) bool {
		if wordN > 1 && start == len(word) {
			return true
		}

		if !visited[start] {
			return false
		}

		for end := start + 1; end <= len(word); end++ {
			if wordMap[word[start:end]] {
				if dfs(word, end, wordN+1) {
					return true
				}
			}
		}
		visited[start] = false

		return false
	}
	for _, word := range words {
		for i := 0; i < len(word); i++ {
			visited[i] = true
		}

		if dfs(word, 0, 0) {
			result = append(result, word)
		}
	}
	return result
}
