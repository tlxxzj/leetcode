func longestSubstring(s string, k int) int {
	n := len(s)
	freqs := make([][26]int, n)
	for i := 0; i < n; i++ {
		freqs[i] = [26]int{}
		if i > 0 {
			for j := 0; j < 26; j++ {
				freqs[i][j] = freqs[i-1][j]
			}
		}
		freqs[i][s[i]-'a']++
	}

    //fmt.Println(freqs[n-1])

	var find func(begin, end int) int
	find = func(begin, end int) int {
		if begin > end || end-begin+1 < k {
			return 0
		}

		f := [26]int{}
		if begin == 0 {
			f = freqs[end]
		} else {
			for i := 0; i < 26; i++ {
				f[i] = freqs[end][i] - freqs[begin-1][i]
			}
		}

		ret := 0
		p := begin
		for i := begin; i <= end; i++ {
			if f[s[i]-'a'] < k {
				ret = max(ret, find(p, i-1))
				p = i + 1
			}
		}
		if p == begin {
			ret = end - begin + 1
		} else {
			ret = max(ret, find(p, end))
		}
        //fmt.Println(begin, end, p, ret, f)
		return ret
	}

	return find(0, n-1)
}
