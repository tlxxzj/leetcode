class RLEIterator:

    def __init__(self, A: List[int]):
        A.reverse()
        self.a = A
        self.x = 0
        self.y = 0

    def next(self, n: int) -> int:
        ret = -1
        while n > 0:
            if self.x == 0:
                if len(self.a) > 0:
                    self.x, self.y = self.a.pop(), self.a.pop()
                else:
                    break
            k = min(self.x, n)
            n -= k
            self.x -= k
            if n == 0:
                ret = self.y
        return ret

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)