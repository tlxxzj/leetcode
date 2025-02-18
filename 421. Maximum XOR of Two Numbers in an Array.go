func findMaximumXOR(nums []int) int {
	const HIGH_BIT = 30
	c := 0
	for i := HIGH_BIT; i >= 0; i-- {
		nums2 := make(map[int]bool)
		for _, num := range nums {
			nums2[num>>i] = true
		}

		found := false
		c = c*2 + 1
		for _, num := range nums {
			if nums2[c^(num>>i)] {
				found = true
				break
			}
		}

		if !found {
			c = c - 1
		}
	}
	return c
}