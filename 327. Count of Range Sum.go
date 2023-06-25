func countRangeSum(nums []int, lower int, upper int) int {
	n := len(nums)
	if n == 0 {
		return 0
	}

	sums := make([]int, len(nums))
	tmp := make([]int, len(nums))
	sums[0] = nums[0]
	for i := 1; i < n; i++ {
		sums[i] = sums[i-1] + nums[i]
	}

	res := 0
	for i := 0; i < n; i++ {
		if sums[i] >= lower && sums[i] <= upper {
			res++
		}
	}
	var merge func(l, r int)
	merge = func(l, r int) {
		if r-l <= 1 {
			return
		}
		m := (l + r) / 2
		merge(l, m)
		merge(m, r)

		i, j, k := l, m, m
		for ; i < m; i++ {
			for j < r && sums[j]-sums[i] < lower {
				j++
			}
			for k < r && sums[k]-sums[i] <= upper {
				k++
			}
			res += k - j
		}

		i, j, k = l, m, 0
		for ; i < m && j < r; k++ {
			if sums[i] < sums[j] {
				tmp[k] = sums[i]
				i++
			} else {
				tmp[k] = sums[j]
				j++
			}
		}
		for ; i < m; i++ {
			tmp[k] = sums[i]
			k++
		}
		for ; j < r; j++ {
			tmp[k] = sums[j]
			k++
		}
		for i := 0; i < k; i++ {
			sums[l+i] = tmp[i]
		}
	}
	merge(0, n)
	return res
}