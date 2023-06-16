func circularArrayLoop(nums []int) bool {
	n := len(nums)
	if n < 2 {
		return false
	}

	next := func(index int) int {
		return ((index+nums[index])%n + n) % n
	}

	for i := 0; i < n; i++ {
		if nums[i] == 0 {
			continue
		}
		slow, fast := i, next(i)
		if slow == fast {
			nums[i] = 0
			continue
		}

		for nums[slow]*nums[fast] > 0 && nums[slow]*nums[next(fast)] > 0 {
			if slow == fast {
				if slow == next(slow) {
					break
				}
				return true
			}
			slow = next(slow)
			fast = next(next(fast))
		}
		for j := i; nums[j] != 0 && ((nums[j] < 0) == (nums[i] < 0)); j = next(j) {
			nums[j] = 0
		}
	}
	return false
}
