type MagicDictionary struct {
	children [26]*MagicDictionary
	isWord   bool
}

func Constructor() MagicDictionary {
	return MagicDictionary{}
}

func (this *MagicDictionary) BuildDict(dictionary []string) {
	for _, word := range dictionary {
		node := this
		for _, c := range word {
			i := c - 'a'
			if node.children[i] == nil {
				node.children[i] = &MagicDictionary{}
			}
			node = node.children[i]
		}
		node.isWord = true
	}
}

func (this *MagicDictionary) Search(searchWord string) bool {
	n := len(searchWord)

	var dfs func(node *MagicDictionary, i int, changed bool) bool

	dfs = func(node *MagicDictionary, i int, changed bool) bool {
		if node == nil {
			return false
		}

		if i == n {
			return node.isWord && changed
		}

		if !changed {
			for j := 0; j < 26; j++ {
				if dfs(node.children[j], i+1, int(searchWord[i]-'a') != j) {
					return true
				}
			}
		} else {
			return dfs(node.children[searchWord[i]-'a'], i+1, true)
		}
		return false
	}

	return dfs(this, 0, false)
}
