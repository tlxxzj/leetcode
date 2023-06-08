func ladderLength(beginWord string, endWord string, wordList []string) int {

	diff1 := func(a, b string) bool {
		diff := 0
		for i := 0; i < len(a); i++ {
			if a[i] != b[i] {
				diff++
				if diff > 1 {
					return false
				}
			}
		}
		return diff == 1
	}

	endWorldExist := false
	wordList = append(wordList, beginWord)
	adjWorlds := make(map[string][]string)
	for i := 0; i < len(wordList); i++ {
		if wordList[i] == endWord {
			endWorldExist = true
		}
		for j := i + 1; j < len(wordList); j++ {
			if diff1(wordList[i], wordList[j]) {
				adjWorlds[wordList[i]] = append(adjWorlds[wordList[i]], wordList[j])
				adjWorlds[wordList[j]] = append(adjWorlds[wordList[j]], wordList[i])
			}
		}
	}

	if !endWorldExist {
		return 0
	}

	visited := make(map[string]bool)
	queue := make([]string, 0)
	queue = append(queue, beginWord)
	visited[beginWord] = true

	step := 1
	for len(queue) > 0 {
		queue2 := make([]string, 0)
		for _, world := range queue {
			if world == endWord {
				return step
			}

			for _, adj := range adjWorlds[world] {
				if !visited[adj] {
					queue2 = append(queue2, adj)
					visited[adj] = true
				}
			}
		}
		step++
		queue = queue2
	}

	return 0
}