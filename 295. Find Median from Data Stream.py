import heapq as hq

class Heap:
    def __init__(self, reverse=False):
        self._data = []
        self._reverse = reverse
    
    def push(self, x):
        if self._reverse:
            hq.heappush(self._data, -x)
        else:
            hq.heappush(self._data, x)
    
    def pop(self):
        if self._reverse:
            return -hq.heappop(self._data)
        else:
            return hq.heappop(self._data)
    
    def front(self):
        if self._reverse:
            return -self._data[0]
        else:
            return self._data[0]
    
    def size(self):
        return len(self._data)


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._minq = Heap()
        self._maxq = Heap(reverse=True)
    
    def addNum(self, num: int) -> None:
        if self._maxq.size() == 0 or num <= self._maxq.front():
            self._maxq.push(num)
        else:
            self._minq.push(num)
        
        if self._maxq.size() - self._minq.size() > 1:
            self._minq.push(self._maxq.pop())
        elif self._minq.size() - self._maxq.size() >= 1:
            self._maxq.push(self._minq.pop())

    def findMedian(self) -> float:
        if (self._maxq.size() + self._minq.size()) % 2 == 1:
            return self._maxq.front()
        else:
            return (self._maxq.front() + self._minq.front()) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()