func maxDistance(arrays [][]int) int {
	abs := func(a int) int {
		if a < 0 {
			return -a
		}
		return a
	}

	res := 0

	minVal := arrays[0][0]
	maxVal := arrays[0][len(arrays[0])-1]

	for i := 1; i < len(arrays); i++ {
		res = max(res, abs(arrays[i][0]-maxVal), abs(arrays[i][len(arrays[i])-1]-minVal))
		minVal = min(minVal, arrays[i][0])
		maxVal = max(maxVal, arrays[i][len(arrays[i])-1])
	}

	return res
}
