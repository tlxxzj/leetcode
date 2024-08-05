func leastBricks(wall [][]int) int {
	row := len(wall)
	if row == 0 {
		return 0
	}

	nums := []int{0}
	for i := 0; i < row; i++ {
		sum := 0
		col := len(wall[i])
		for j := 0; j < col; j++ {
			sum += wall[i][j]
			nums = append(nums, sum)
		}
	}

	slices.Sort(nums)
	//fmt.Println(nums)

	m := make(map[int]int)
	m[0] = 0
	prevNum := 0
	maxM := 0
	for i, num := range nums {
		if i == 0 {
			continue
		}
		if num == nums[i-1] {
			continue
		}

		if num-prevNum == 1 {
			m[num] = m[prevNum] + 2
		} else {
			m[num] = m[prevNum] + 2
		}
		prevNum = num
		maxM = m[num]
	}
	//fmt.Println(m)

	bricks := make([]int, maxM)
	for i := 0; i < row; i++ {
		sum := 0
		col := len(wall[i])
		for j := 0; j < col; j++ {
			//start := m[sum]
			sum += wall[i][j]
			end := m[sum]
			if end < maxM {
				bricks[end]++
			}
		}
	}
	//fmt.Println(bricks)
	return row - slices.Max(bricks)
}
