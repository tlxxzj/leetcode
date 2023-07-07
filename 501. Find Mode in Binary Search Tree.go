/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func findMode(root *TreeNode) []int {
	res := []int{}
	val, count, maxCount := 0, 0, 0

	var find func(node *TreeNode)
	find = func(node *TreeNode) {
		if node == nil {
			return
		}
		find(node.Left)
		if node.Val == val {
			count++
		} else {
			val = node.Val
			count = 1
		}
		if count == maxCount {
			res = append(res, val)
		} else if count > maxCount {
			maxCount = count
			res = []int{val}
		}
		find(node.Right)
	}
	find(root)
	return res
}