type NumArray struct {
	nums []int
	sums []int
}

func lowbit(x int) int {
	return x & (-x)
}

func (this *NumArray) sum(x int) int {
	res := 0
	for i := x; i > 0; i -= lowbit(i) {
		res += this.sums[i]
	}
	return res
}

func Constructor(nums []int) NumArray {
	arr := NumArray{
		nums: make([]int, len(nums)),
		sums: make([]int, len(nums)+1),
	}
	for i := 0; i < len(nums); i++ {
		arr.Update(i, nums[i])
	}
	return arr
}

func (this *NumArray) Update(index int, val int) {
	delta := val - this.nums[index]
	this.nums[index] = val

	for i := index + 1; i < len(this.sums); i += lowbit(i) {
		this.sums[i] += delta
	}
}

func (this *NumArray) SumRange(left int, right int) int {
	return this.sum(right+1) - this.sum(left)
}

/**
 * Your NumArray object will be instantiated and called as such:
 * obj := Constructor(nums);
 * obj.Update(index,val);
 * param_2 := obj.SumRange(left,right);
 */

/**
 * Your NumMatrix object will be instantiated and called as such:
 * obj := Constructor(matrix);
 * param_1 := obj.SumRegion(row1,col1,row2,col2);
 */
