class MyCircularQueue:

    def __init__(self, k: int):
        self._data = [0] * k
        self._k = k
        self._size = 0
        self._f = 0
        self._r = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self._size += 1
        self._data[self._r] = value
        self._r = (self._r + 1) % self._k
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self._size -= 1
        self._f = (self._f + 1) % self._k
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self._data[self._f]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self._data[self._r-1]

    def isEmpty(self) -> bool:
        return self._size == 0

    def isFull(self) -> bool:
        return self._size == self._k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()