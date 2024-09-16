func wiggleSort(nums []int) {
	n := len(nums)
	sortedNums := make([]int, n)
	copy(sortedNums, nums)
	slices.Sort(sortedNums)
	i := (n - 1) / 2
	j := n - 1
	for k := 0; k < n; {
		nums[k] = sortedNums[i]
		i--
		k++
		if k < n {
			nums[k] = sortedNums[j]
			j--
			k++
		}
	}
}
