func leastBricks(wall [][]int) int {
	row := len(wall)
	if row == 0 {
		return 0
	}

	bricks := make(map[int]int)
	for _, row := range wall {
		sum := 0
		for i, num := range row {
			if i != len(row)-1 {
				sum += num
				bricks[sum]++
			}
		}
	}
	maxCount := 0
	for _, count := range bricks {
		if count > maxCount {
			maxCount = count
		}
	}
	return row - maxCount
}
