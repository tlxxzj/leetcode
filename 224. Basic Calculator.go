func calculate(s string) int {
	n := len(s)
	res := 0
	sign := 1
	ops := []int{1}

	for i := 0; i < n; {
		c := s[i]
		if c == ' ' {
			i++
			continue
		}

		if c == '+' {
			i++
            sign = ops[len(ops)-1]
		} else if c == '-' {
			i++
			sign = -ops[len(ops)-1]
		} else if c == '(' {
			i++
			ops = append(ops, sign)
		} else if c == ')' {
			i++
			ops = ops[:len(ops)-1]
		} else {
			num := 0
			for i < n && s[i] >= '0' && s[i] <= '9' {
				num = num*10 + int(s[i]-'0')
				i++
			}
			res += sign * num
		}
	}

	return res
}
