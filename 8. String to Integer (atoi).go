func myAtoi(s string) int {
	res := int64(0)
	sign := 1
	n := len(s)
	i := 0

	// skip leading spaces
	for i < n && s[i] == ' ' {
		i++
	}
	// check sign
	if i < n && s[i] == '+' {
		i++
	} else if i < n && s[i] == '-' {
		sign = -1
		i++
	}
	// convert number and avoid overflow
	for i < n && s[i] >= '0' && s[i] <= '9' {
		res = res*10 + int64(s[i]-'0')
		if sign == 1 && res > math.MaxInt32 {
			return math.MaxInt32
		} else if sign == -1 && res > int64(math.MaxInt32)+1 {
			return math.MinInt32
		}
		i++
	}
	return sign * int(res)
}