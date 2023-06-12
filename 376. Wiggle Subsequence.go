func wiggleMaxLength(nums []int) int {
	n := len(nums)
	if n < 2 {
		return n
	}
	res := 1
	preNum := nums[0]
	lastDiff := 0
	for i := 1; i < n; i++ {
		if nums[i] == preNum {
			continue
		}

		if res == 1 {
			res++
			lastDiff = nums[i] - preNum
			preNum = nums[i]
		} else {
			diff := nums[i] - preNum
			if diff*lastDiff < 0 {
				res++
			}
			lastDiff = diff
			preNum = nums[i]
		}
	}
	return res
}