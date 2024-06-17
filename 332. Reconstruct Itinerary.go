func findItinerary(tickets [][]string) []string {
	n := len(tickets)

	edges := make(map[string]int)
	edgeMap := make(map[string][]string)
	for _, ticket := range tickets {
		from, to := ticket[0], ticket[1]
		edgeMap[from] = append(edgeMap[from], to)
		edges[from+"-"+to]++
	}

	for from, tos := range edgeMap {
		slices.Sort(tos)
		uniqueTos := make([]string, 0)
		for i := 0; i < len(tos); i++ {
			if i == 0 || tos[i] != tos[i-1] {
				uniqueTos = append(uniqueTos, tos[i])
			}
		}
		edgeMap[from] = uniqueTos
	}

	res := make([]string, 0)
	var dfs func(from string, step int) bool
	dfs = func(from string, step int) bool {
		if step == n {
			return true
		}

		if tos, ok := edgeMap[from]; ok {
			for _, to := range tos {
				if edges[from+"-"+to] > 0 {
					edges[from+"-"+to]--
					res = append(res, to)
					if dfs(to, step+1) {
						return true
					}
					res = res[:len(res)-1]
					edges[from+"-"+to]++
				}
			}
		}
		return false
	}

	res = append(res, "JFK")
	dfs("JFK", 0)
	return res
}
