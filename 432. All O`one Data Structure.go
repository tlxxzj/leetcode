
import "container/list"

type AllOne struct {
	count    map[string]int
	str2node map[string]*list.Element
	strs     *list.List
}

func Constructor() AllOne {
	return AllOne{
		count:    make(map[string]int),
		str2node: make(map[string]*list.Element),
		strs:     list.New(),
	}
}

func (this *AllOne) Inc(key string) {
	this.count[key]++
	c := this.count[key]
	if c == 1 {
		e := this.strs.PushBack(key)
		this.str2node[key] = e
	} else {
		e := this.str2node[key]
		prev := e.Prev()
		for prev != nil && this.count[prev.Value.(string)] < c {
			prev = prev.Prev()
		}
		if prev != nil {
			this.strs.MoveAfter(e, prev)
		} else {
			this.strs.MoveToFront(e)
		}
	}
}

func (this *AllOne) Dec(key string) {
	this.count[key]--
	c := this.count[key]
	if c == 0 {
		delete(this.count, key)
		e := this.str2node[key]
		this.strs.Remove(e)
	} else {
		e := this.str2node[key]
		next := e.Next()
		for next != nil && this.count[next.Value.(string)] > c {
			next = next.Next()
		}
		if next != nil {
			this.strs.MoveBefore(e, next)
		} else {
			this.strs.MoveToBack(e)
		}
	}
}

func (this *AllOne) GetMaxKey() string {
	if this.strs.Len() == 0 {
		return ""
	}
	return this.strs.Front().Value.(string)
}

func (this *AllOne) GetMinKey() string {
	if this.strs.Len() == 0 {
		return ""
	}
	return this.strs.Back().Value.(string)
}
