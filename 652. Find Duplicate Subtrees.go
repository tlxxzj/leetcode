func findDuplicateSubtrees(root *TreeNode) []*TreeNode {
	trees := map[string]int{}
	duplicates := []*TreeNode{}

	var preOrder func(*TreeNode) string

	preOrder = func(node *TreeNode) string {
		if node == nil {
			return "#"
		}
		left := preOrder(node.Left)
		right := preOrder(node.Right)
		subtree := fmt.Sprintf("%d,%s,%s", node.Val, left, right)
		trees[subtree]++
		if trees[subtree] == 2 {
			duplicates = append(duplicates, node)
		}
		return subtree
	}

	preOrder(root)
	return duplicates

}
