func trap(height []int) int {
	res := 0
	l, r := 0, len(height)-1
	lmax, rmax := height[l], height[r]

	max := func(a, b int) int {
		if a < b {
			return b
		} else {
			return a
		}
	}

	for l < r {
		lmax = max(lmax, height[l])
		rmax = max(rmax, height[r])
		if lmax < rmax {
			res += lmax - height[l]
			l++
		} else {
			res += rmax - height[r]
			r--
		}
	}
	return res
}