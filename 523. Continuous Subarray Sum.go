
func checkSubarraySum(nums []int, k int) bool {
	n := len(nums)
	if n < 2 {
		return false
	}
	sum := 0
	mp := make(map[int]int)
	for i := 0; i < n; i++ {
		nums[i] = nums[i] % k
		if i > 0 && nums[i] == 0 && nums[i-1] == 0 {
			return true
		}
		if nums[i] == 0 {
			continue
		}
		sum = (sum + nums[i]) % k
		if sum == 0 && i > 0 {
			return true
		}
		if _, ok := mp[sum]; ok {
			return true
		}
		mp[sum] = i
	}
	return false
}
