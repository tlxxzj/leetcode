func findWords(board [][]byte, words []string) []string {
	type Trie struct {
		children [26]*Trie
		word     string
		isWord   bool
	}

	m, n := len(board), len(board[0])
	res := []string{}
	trie := &Trie{}

	visited := make([][]bool, m)
	for i := range visited {
		visited[i] = make([]bool, n)
	}

	insert := func(t *Trie, word string) {
		for _, c := range word {
			if t.children[c-'a'] == nil {
				t.children[c-'a'] = &Trie{}
			}
			t = t.children[c-'a']
		}
		t.word = word
		t.isWord = true
	}

	for _, word := range words {
		insert(trie, word)
	}

	var dfs func(t *Trie, i, j int)
	dfs = func(t *Trie, i, j int) {
		if i < 0 || i >= m || j < 0 || j >= n || visited[i][j] {
			return
		}

		visited[i][j] = true
		k := int(board[i][j] - 'a')
		if t.children[k] != nil {
			t = t.children[k]
			if t.isWord {
				res = append(res, t.word)
				t.isWord = false
			}

			dfs(t, i+1, j)
			dfs(t, i-1, j)
			dfs(t, i, j+1)
			dfs(t, i, j-1)
		}

		visited[i][j] = false
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			dfs(trie, i, j)
		}
	}

	return res
}
