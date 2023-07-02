func singleNumber(nums []int) []int {
	res := make([]int, 2)
	x := 0
	for _, v := range nums {
		x ^= v
	}
	x = x & (-x)
	for _, v := range nums {
		if v&x == 0 {
			res[0] ^= v
		} else {
			res[1] ^= v
		}
	}
	return res
}
