func canMeasureWater(jug1Capacity int, jug2Capacity int, targetCapacity int) bool {
    var gcd func(int, int) int
	gcd = func(a, b int) int {
		if b == 0 {
			return a
		}
		return gcd(b, a%b)
	}
	return targetCapacity <= jug1Capacity+jug2Capacity && targetCapacity%gcd(jug1Capacity, jug2Capacity) == 0
}