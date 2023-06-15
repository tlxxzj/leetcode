func firstMissingPositive(nums []int) int {
	n := len(nums)
	if n == 0 {
		return 1
	}
	swap := func(i, j int) {
		nums[i], nums[j] = nums[j], nums[i]
	}
	for i := 0; i < n; i++ {
		for nums[i] > 0 && nums[i] <= n && i+1 != nums[i] && nums[i] != nums[nums[i]-1] {
			swap(i, nums[i]-1)
		}
	}
	for i := 0; i < n; i++ {
		if i+1 != nums[i] {
			return i + 1
		}
	}
	return nums[n-1] + 1
}