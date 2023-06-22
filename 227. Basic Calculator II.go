func calculate(s string) int {
	nums := make([]any, 0)
	n := len(s)
	for i := 0; i < n; i++ {
		if s[i] == ' ' {
			continue
		}
		if s[i] == '+' || s[i] == '-' || s[i] == '*' || s[i] == '/' {
			nums = append(nums, s[i])
		} else {
			num := 0
			for i < n && s[i] >= '0' && s[i] <= '9' {
				num = num*10 + int(s[i]-'0')
				i++
			}
			nums = append(nums, num)
			i--
		}
	}

	nums2 := make([]any, 0)
	for i := 0; i < len(nums); i++ {
		if op, ok := nums[i].(uint8); ok && (op == '*' || op == '/') {
			a := nums2[len(nums2)-1].(int)
			b := nums[i+1].(int)
			if op == '*' {
				nums2[len(nums2)-1] = a * b
			} else {
				nums2[len(nums2)-1] = a / b
			}
			i++
		} else {
			nums2 = append(nums2, nums[i])
		}
	}

	nums = nums2
	nums2 = make([]any, 0)
	for i := 0; i < len(nums); i++ {
		if op, ok := nums[i].(uint8); ok {
			a := nums2[len(nums2)-1].(int)
			b := nums[i+1].(int)
			if op == '+' {
				nums2[len(nums2)-1] = a + b
			} else {
				nums2[len(nums2)-1] = a - b
			}
			i++
		} else {
			nums2 = append(nums2, nums[i])
		}
	}
	return nums2[0].(int)
}
