class Solution:

    def __init__(self, w: List[int]):
        n = len(w)
        ws = [0] * n
        ws[0] = w[0]
        for i in range(1, n):
            ws[i] = ws[i-1] + w[i]
        self.n = n
        self.ws = ws

    def pickIndex(self) -> int:
        from random import randint
        x = randint(1, self.ws[-1])
        l, r = 0, self.n
        while l < r:
            m = (l + r) >> 1
            if x <= self.ws[m]:
                r = m
            else:
                l = m + 1
        return r
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()