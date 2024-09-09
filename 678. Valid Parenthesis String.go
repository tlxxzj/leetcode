func checkValidString(s string) bool {
	left := 0
	stack := []rune{}
	for _, c := range s {
		if c == '(' || c == '*' {
			if c == '(' {
				left++
			}
			stack = append(stack, c)
		} else {
			if len(stack) == 0 {
				return false
			}
			if left == 0 {
				// pop * as '('
				stack = stack[:len(stack)-1]
			} else {
				// find and pop '('
				left--
				for i := len(stack) - 1; i >= 0; i-- {
					if stack[i] == '(' {
						for j := i; j < len(stack)-1; j++ {
							stack[j] = stack[j+1]
						}
						stack = stack[:len(stack)-1]
						break
					}
				}
			}
		}
	}

	if left == 0 {
		return true
	}

	// check if there are enough * to replace ')'
	star := 0
	for i := len(stack) - 1; i >= 0; i-- {
		if stack[i] == '*' {
			star++
		} else if star > 0 {
			star--
		} else {
			return false
		}
	}
	return true
}
