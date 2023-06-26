func kSmallestPairs(nums1 []int, nums2 []int, k int) [][]int {
	n1, n2 := len(nums1), len(nums2)
	res := make([][]int, 0, k)

	first := make([][2]int, 0, n1)
	first = append(first, [2]int{0, 0})

	for len(res) < k && len(first) > 0 {
		min := math.MaxInt32
		for j := 0; j < len(first); j++ {
			sum := nums1[first[j][0]] + nums2[first[j][1]]
			if sum < min {
				min = sum
			}
		}
		if first[len(first)-1][0]+1 < n1 && nums1[first[len(first)-1][0]+1]+nums2[0] <= min {
			first = append(first, [2]int{first[len(first)-1][0] + 1, 0})
			min = nums1[first[len(first)-1][0]] + nums2[0]
		}

		offset := 0
		for j := 0; j < len(first) && len(res) < k; j++ {
			sum := nums1[first[j][0]] + nums2[first[j][1]]
			if sum == min {
				res = append(res, []int{nums1[first[j][0]], nums2[first[j][1]]})
				first[j][1]++
				if first[j][1] == n2 {
					offset++
					if offset == len(first) && first[len(first)-1][0]+1 < n1 {
						first = append(first, [2]int{first[len(first)-1][0] + 1, 0})
					}
				}
			}
		}
		first = first[offset:]
	}
	return res
}