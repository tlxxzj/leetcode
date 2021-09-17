class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.i = 0
        self.l = len(self.encoding)
        self.val = 0
        self.t = 0

    def next(self, n: int) -> int:
        val = -1
        while n > 0:
            if self.t > 0:
                x = min(n, self.t)
                n -= x
                self.t -= x
                val = self.val
            else:
                if self.i + 1 >= self.l:
                    return -1
                self.t = self.encoding[self.i]
                self.val = self.encoding[self.i + 1]
                self.i = self.i + 2
        return val

        
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)