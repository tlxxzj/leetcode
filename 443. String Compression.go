func compress(chars []byte) int {
	n := len(chars)
	if n <= 1 {
		return n
	}

	res := 0
	cnt := 1
	for i := 1; i <= n; i++ {
		if i == n || chars[i] != chars[i-1] {
			chars[res] = chars[i-1]
			res++
			if cnt > 1 {
				s := strconv.Itoa(cnt)
				for j := 0; j < len(s); j++ {
					chars[res] = s[j]
					res++
				}
			}
			cnt = 1
		} else {
			cnt++
		}
	}
	return res
}