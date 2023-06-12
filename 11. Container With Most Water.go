func maxArea(height []int) int {
	res := 0
	l, r := 0, len(height)-1
	lmax, rmax := height[l], height[r]

	max := func(a, b int) int {
		if a < b {
			return b
		}
		return a
	}

	for l < r {
		lmax = max(lmax, height[l])
		rmax = max(rmax, height[r])
		if lmax < rmax {
			res = max(res, lmax*(r-l))
			l++
		} else {
			res = max(res, rmax*(r-l))
			r--
		}
	}
	return res
}