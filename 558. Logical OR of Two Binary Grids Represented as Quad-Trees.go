func intersect(quadTree1 *Node, quadTree2 *Node) *Node {
	if quadTree1 == nil && quadTree2 == nil {
		return nil
	}

	node := &Node{}

	if !quadTree1.IsLeaf && quadTree2.IsLeaf {
		quadTree1, quadTree2 = quadTree2, quadTree1
	}

	if quadTree1.IsLeaf {
		if quadTree1.Val {
			*node = *quadTree1
		} else {
			*node = *quadTree2
		}
	} else {
		node.TopLeft = intersect(quadTree1.TopLeft, quadTree2.TopLeft)
		node.TopRight = intersect(quadTree1.TopRight, quadTree2.TopRight)
		node.BottomLeft = intersect(quadTree1.BottomLeft, quadTree2.BottomLeft)
		node.BottomRight = intersect(quadTree1.BottomRight, quadTree2.BottomRight)

		if node.TopLeft.IsLeaf && node.TopRight.IsLeaf && node.BottomLeft.IsLeaf && node.BottomRight.IsLeaf &&
			node.TopLeft.Val == node.TopRight.Val && node.TopRight.Val == node.BottomLeft.Val && node.BottomLeft.Val == node.BottomRight.Val {
			node.IsLeaf = true
			node.Val = node.TopLeft.Val
			node.TopLeft, node.TopRight, node.BottomLeft, node.BottomRight = nil, nil, nil, nil
		}
	}

	return node
}
