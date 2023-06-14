func longestValidParentheses(s string) int {
	res := 0
	valid := make([]int, len(s))
	stack := []int{}
	for i := range s {
		if s[i] == '(' {
			stack = append(stack, i)
		} else if len(stack) > 0 {
			p := stack[len(stack)-1]
			if s[p] == '(' {
				stack = stack[:len(stack)-1]
				valid[i] = i - p + 1
				if p > 0 {
					valid[i] += valid[p-1]
				}
				if valid[i] > res {
					res = valid[i]
				}
			}
		}
	}
	return res
}