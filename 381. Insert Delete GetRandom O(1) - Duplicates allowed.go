type RandomizedCollection struct {
	data   []*int
	indexs map[int][]int
	unused []int
	len    int
	cap    int
}

func Constructor() RandomizedCollection {
	return RandomizedCollection{
		data:   make([]*int, 0),
		indexs: make(map[int][]int),
		unused: make([]int, 0),
		len:    0,
		cap:    0,
	}
}

func (this *RandomizedCollection) Insert(val int) bool {
	if this.len == this.cap {
		newData := make([]*int, this.cap*2+1)
		newCap := len(newData)
		k := 0
		for i := 0; i < this.cap; i++ {
			if this.data[i] != nil {
				newData[k] = this.data[i]
				k++
			}
		}
		this.data = newData
		this.cap = newCap
	}

	index := -1
	if len(this.unused) > 0 {
		index = this.unused[len(this.unused)-1]
		this.unused = this.unused[:len(this.unused)-1]
	} else {
		index = this.len
	}

	this.data[index] = &val
	this.indexs[val] = append(this.indexs[val], index)
	this.len++

	return len(this.indexs[val]) == 1
}

func (this *RandomizedCollection) Remove(val int) bool {
	if len(this.indexs[val]) == 0 {
		return false
	}

	indexs := this.indexs[val]
	index := indexs[len(indexs)-1]
	indexs = indexs[:len(indexs)-1]
	if len(indexs) == 0 {
		delete(this.indexs, val)
	} else {
		this.indexs[val] = indexs
	}

	this.data[index] = nil
	this.unused = append(this.unused, index)
	this.len--

	return true
}

func (this *RandomizedCollection) GetRandom() int {
	if this.len == 0 {
		return 0
	}

	for {
		index := rand.Intn(this.cap)
		if this.data[index] != nil {
			return *this.data[index]
		}
	}
}


/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */
