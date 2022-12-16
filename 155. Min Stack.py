class MinStack:

    def __init__(self):
        self._a = []
        self._min = None

    def push(self, val: int) -> None:
        if len(self._a) == 0 or val < self._min:
            self._min = val
        self._a.append((val, self._min))

    def pop(self) -> None:
        val, m = self._a.pop()
        if val == m:
            if len(self._a) == 0:
                self._min = None
            else:
                self._min = self._a[-1][1]
        return val

    def top(self) -> int:
        return self._a[-1][0]

    def getMin(self) -> int:
        return self._a[-1][1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()