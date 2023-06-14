func findSubstring(s string, words []string) []int {
	res := make([]int, 0)

	n := len(s)
	wn, wl := len(words), len(words[0])
	if n < wn*wl {
		return res
	}

	// words map
	nWorld := 0
	wm := make(map[string]int)
	for _, w := range words {
		if wm[w] == 0 {
			nWorld++
		}
		wm[w]++
	}

	// sliding window
	for i := 0; i < wl; i++ {
		// reset
		start := i
		wm2 := make(map[string]int)
		nWorld2 := 0
		for j := i; j+wl <= n; j += wl {
			w := s[j : j+wl]
			if wm[w] == 0 {
				start = j + wl
				wm2 = make(map[string]int)
				nWorld2 = 0
			} else {
				wm2[w]++
				if wm2[w] == wm[w] {
					nWorld2++
				} else {
					for wm2[w] > wm[w] {
						w2 := s[start : start+wl]
						if wm2[w2] == wm[w2] {
							nWorld2--
						}
						wm2[w2]--
						start += wl
					}
				}
				if nWorld2 == nWorld {
					res = append(res, start)
				}
			}
		}
	}
	return res
}