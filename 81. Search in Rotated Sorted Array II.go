func search(nums []int, target int) bool {
	n := len(nums)
	l, r := 0, n-1
	for l <= r {
		m := (l + r) / 2
		if nums[m] == target {
			return true
		}
        for l <m && nums[l] == nums[m] {
            l++
        }
        for m <r && nums[r] == nums[m] {
            r--
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
	return false
}
