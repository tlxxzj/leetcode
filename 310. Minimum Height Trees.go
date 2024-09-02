func findMinHeightTrees(n int, edges [][]int) []int {
	if n == 1 {
		return []int{0}
	} else if n == 2 {
		return []int{0, 1}
	}

	nodes := make([][]int, n)
	parents := make([]int, n)

	for _, edge := range edges {
		a, b := edge[0], edge[1]
		nodes[a] = append(nodes[a], b)
		nodes[b] = append(nodes[b], a)
	}

	findFarthest := func(start int) (int, int) {
		queue := [][2]int{{start, 0}}
		visited := make([]bool, n)
		visited[start] = true
		last := start
		lastDist := 0
		for len(queue) > 0 {
			node, dist := queue[0][0], queue[0][1]
			last = node
			lastDist = dist
			queue = queue[1:]
			for _, next := range nodes[node] {
				if !visited[next] {
					visited[next] = true
					queue = append(queue, [2]int{next, dist + 1})
					parents[next] = node
				}
			}
		}
		return last, lastDist
	}

	x := 0
	y, _ := findFarthest(x)
	y, dist := findFarthest(y)

	var roots []int
	node := y
	for i := dist / 2; i > 0; i-- {
		node = parents[node]
	}

	if dist%2 == 0 {
		roots = []int{node}
	} else {
		roots = []int{node, parents[node]}
	}

	return roots
}
