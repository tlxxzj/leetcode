func increasingTriplet(nums []int) bool {
	n := len(nums)
	if n < 3 {
		return false
	}
	maxP := 0
	for i := 0; i < n; i++ {
		j := maxP
		for j >= 0 && nums[i] <= nums[j] {
			j--
		}
		nums[j+1] = nums[i]
		if j+1 > maxP {
			maxP = j + 1
			if maxP == 2 {
				return true
			}
		}
	}
	return false
}
