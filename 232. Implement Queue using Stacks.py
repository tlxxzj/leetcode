class MyQueue:

    def __init__(self):
        self._s1 = []
        self._s2 = []
    
    def _getq(self):
        if len(self._s1) == 0:
            self._s1, self._s2 = self._s2, self._s1
            self._s1.reverse()

    def push(self, x: int) -> None:
        self._s2.append(x)

    def pop(self) -> int:
        self._getq()
        return self._s1.pop()
        
    def peek(self) -> int:
        self._getq()
        return self._s1[-1]

    def empty(self) -> bool:
        return len(self._s1) == 0 and len(self._s2) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()