class MyCircularDeque:
    def __init__(self, k: int):
        self._data = [0] * k
        self._k = k
        self._size = 0
        self._f = 0
        self._r = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self._size == 0:
            self._r = (self._f + 1) % self._k
        self._data[self._f] = value
        self._f = (self._f - 1) % self._k
        self._size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self._size == 0:
            self.f = (self._r - 1) % self._k
        self._data[self._r] = value
        self._r = (self._r + 1) % self._k
        self._size += 1
        return True
        
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self._f = (self._f + 1) % self._k
        self._size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self._r = (self._r - 1) % self._k
        self._size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self._data[(self._f + 1) % self._k]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self._data[(self._r - 1) % self._k]

    def isEmpty(self) -> bool:
        return self._size == 0

    def isFull(self) -> bool:
        return self._size == self._k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()