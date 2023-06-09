func search(nums []int, target int) int {
	n := len(nums)
	l, r := 0, n-1
	for l <= r {
		m := (l + r) / 2
		if nums[m] == target {
			return m
		}
		if target < nums[m] {
			if nums[m] <= nums[r] || target >= nums[l] {
				r = m - 1
			} else {
				l = m + 1
			}
		} else {
			if nums[m] >= nums[l] || target <= nums[r] {
				l = m + 1
			} else {
				r = m - 1
			}
		}

	}
	return -1
}
