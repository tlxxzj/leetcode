import "slices"

type Queue struct {
	data1 []string
	data2 []string
}

func (q *Queue) Append(x string) {
	q.data1 = append(q.data1, x)
}

func (q *Queue) Pop() string {
	if len(q.data2) == 0 {
		q.data1, q.data2 = q.data2, q.data1
		slices.Reverse(q.data2)
	}
	x := q.data2[len(q.data2)-1]
	q.data2 = q.data2[:len(q.data2)-1]
	return x
}

func (q *Queue) Empty() bool {
	return len(q.data1) == 0 && len(q.data2) == 0
}

func minMutation(startGene string, endGene string, bank []string) int {
	// check if startGene and endGene are in bank
	startIndex, endIndex := -1, -1
	for i, gene := range bank {
		if gene == startGene {
			startIndex = i
		}
		if gene == endGene {
			endIndex = i
		}
		if startIndex != -1 && endIndex != -1 {
			break
		}
	}
	// if endGene is not in bank, return -1
	if endIndex == -1 {
		return -1
	}
	// if startGene is not in bank, add it to bank
	if startIndex == -1 {
		bank = append(bank, startGene)
	}

	// create a map to store the mutations
	genLen := len(startGene)
	mutations := make(map[string][]string)
	for i := 0; i < len(bank); i++ {
		for j := i + 1; j < len(bank); j++ {
			gen1, gen2 := bank[i], bank[j]
			diff := 0
			for i := 0; i < genLen && diff < 2; i++ {
				if gen1[i] != gen2[i] {
					diff++
				}
			}
			if diff == 1 {
				mutations[gen1] = append(mutations[gen1], gen2)
				mutations[gen2] = append(mutations[gen2], gen1)
			}
		}
	}
    
	// create a map to store the distances
	distances := make(map[string]int)
	distances[startGene] = 0

	// create a queue to store the genes to be visited
	queue := Queue{}
	queue.Append(startGene)
	for !queue.Empty() {
		gene := queue.Pop()
		if gene == endGene {
			return distances[gene]
		}
		for _, mutation := range mutations[gene] {
			if _, ok := distances[mutation]; !ok {
				distances[mutation] = distances[gene] + 1
				queue.Append(mutation)
			}
		}
	}
	return -1
}
