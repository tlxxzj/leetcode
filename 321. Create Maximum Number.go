func maxNumber(nums1 []int, nums2 []int, k int) []int {
	maxN := func(nums []int, k int) []int {
		stack := make([]int, 0)
		for i, num := range nums {
			for len(stack) > 0 && stack[len(stack)-1] < num && len(stack)+len(nums)-i > k {
				stack = stack[:len(stack)-1]
			}
			if len(stack) < k {
				stack = append(stack, num)
			}
		}
		return stack
	}

	merge := func(nums1, nums2 []int) []int {
		nums := make([]int, 0)
		i, j := 0, 0
		for i < len(nums1) || j < len(nums2) {
			if i == len(nums1) {
				nums = append(nums, nums2[j:]...)
				break
			}
			if j == len(nums2) {
				nums = append(nums, nums1[i:]...)
				break
			}
			if nums1[i] < nums2[j] {
				nums = append(nums, nums2[j])
				j++
			} else if nums1[i] > nums2[j] {
				nums = append(nums, nums1[i])
				i++
			} else {
				k := 0
				for i+k < len(nums1) && j+k < len(nums2) && nums1[i+k] == nums2[j+k] {
					k++
				}
				if i+k == len(nums1) {
					nums = append(nums, nums2[j])
					j++
				} else if j+k == len(nums2) {
					nums = append(nums, nums1[i])
					i++
				} else if nums1[i+k] < nums2[j+k] {
					nums = append(nums, nums2[j])
					j++
				} else {
					nums = append(nums, nums1[i])
					i++
				}
			}
		}
		return nums
	}

	max := func(nums1, nums2 []int) []int {
		for i := 0; i < len(nums1); i++ {
			if nums1[i] < nums2[i] {
				return nums2
			} else if nums1[i] > nums2[i] {
				return nums1
			}
		}
		return nums1
	}

	res := make([]int, k)
	for i := 0; i <= k; i++ {
		if i <= len(nums1) && k-i <= len(nums2) {
			res = max(res, merge(maxN(nums1, i), maxN(nums2, k-i)))
		}
	}
	return res
}