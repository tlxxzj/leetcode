func wordBreak(s string, wordDict []string) []string {
	words := make(map[string]int)

	for _, word := range wordDict {
		words[word] = 1
	}

	var res []string
	var dfs func(int, []string)
	dfs = func(start int, path []string) {
		if start == len(s) {
			res = append(res, strings.Join(path, " "))
			return
		}

		for i := start; i < len(s); i++ {
			word := s[start : i+1]
			if words[word] == 1 {
				dfs(i+1, append(path, word))
			}
		}
	}

	dfs(0, nil)
	return res
}
