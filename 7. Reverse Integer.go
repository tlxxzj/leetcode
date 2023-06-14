func reverse(x int) int {
	isOverflowMul := func(x, y int32) bool {
		if x == 0 || y == 0 {
			return false
		}
		if x*y/x != y || x*y/y != x {
			return true
		}
		return false
	}

	isOverflowAdd := func(x, y int32) bool {
		if x == 0 || y == 0 || (x < 0) != (y < 0) {
			return false
		}
		if x > 0 && (x+y < x || x+y < y) {
			return true
		}
		if x < 0 && (x+y > x || x+y > y) {
			return true
		}
		return false
	}
	isOverflowMul(0, 0)
	isOverflowAdd(0, 0)
	var res int32 = 0
	y := 0
	for x != 0 {
		x, y = x/10, x%10
		if isOverflowMul(res, 10) || isOverflowAdd(res*10, int32(y)) {
			return 0
		}
		res = res*10 + int32(y)
	}
	return int(res)
}