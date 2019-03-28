class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        n = len(blacklist)
        m = N - n
        if m <= 100000:
            self.seq = []
            black = set(blacklist)
            for i in range(N):
                if i not in black:
                    self.seq.append(i)
        else:
            self.N = N
            self.black = set(blacklist)
        self.m = m

    def pick(self) -> int:
        if self.m <= 100000:
            return random.choice(self.seq)
        else:
            while 1:
                x = random.randint(0, self.N-1)
                if x not in self.black:
                    return x


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()