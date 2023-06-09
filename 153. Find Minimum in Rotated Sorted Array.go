func findMin(nums []int) int {
	n := len(nums)
	l, r := 0, n-1
	for l < r {
		m := (l + r) / 2
		if nums[m] >= nums[l] && nums[m] >= nums[r] {
			l = m + 1
		} else {
			r = m
		}
	}
	return nums[l]
}