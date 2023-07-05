func validSquare(p1 []int, p2 []int, p3 []int, p4 []int) bool {
	pow2 := func(x int) int {
		return x * x
	}

	valid := func(x, y, z []int) bool {
		a := pow2(x[0]-y[0]) + pow2(x[1]-y[1])
		b := pow2(x[0]-z[0]) + pow2(x[1]-z[1])
		c := pow2(y[0]-z[0]) + pow2(y[1]-z[1])
		return (a == b && a+b == c && c > 0) || (a == c && a+c == b && b > 0) || (b == c && b+c == a && a > 0)
	}

	return valid(p1, p2, p3) && valid(p1, p2, p4) && valid(p1, p3, p4) && valid(p2, p3, p4)
}
