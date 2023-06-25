func thirdMax(nums []int) int {
	a, b, c := math.MinInt64, math.MinInt64, math.MinInt64
	for _, v := range nums {
		if v > a {
			a, b, c = v, a, b
		} else if v < a && v > b {
			b, c = v, b
		} else if v < b && v > c {
			c = v
		}
	}
	if c == math.MinInt64 {
		return a
	}
	return c
}