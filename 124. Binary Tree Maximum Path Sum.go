/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxPathSum(root *TreeNode) int {
	ret := math.MinInt32

	max := func(a, b int) int {
		if a < b {
			return b
		}
		return a
	}

	var dfs func(node *TreeNode) int
	dfs = func(node *TreeNode) int {
		if node == nil {
			return math.MinInt32
		}

		left := max(node.Val, node.Val+dfs(node.Left))
		right := max(node.Val, node.Val+dfs(node.Right))

		ret = max(ret, left+right-node.Val)
		return max(left, right)
	}
	dfs(root)

	return ret
}