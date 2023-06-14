func maxSlidingWindow(nums []int, k int) []int {
	n := len(nums)
	res := make([]int, 0, n)
	slid := make([]int, n)
	l, r := 0, 0

	for i := 0; i < n; i++ {
		if i >= k {
			if l < r && nums[i-k] == slid[l] {
				l++
			}
		}
		for l < r && slid[r-1] < nums[i] {
			r--
		}
		slid[r] = nums[i]
		r++
		if i >= k-1 {
			res = append(res, slid[l])
		}
	}
	return res
}
