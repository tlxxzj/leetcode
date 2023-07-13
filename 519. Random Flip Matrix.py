class Solution:
    def __init__(self, m: int, n: int):
        self._m = m
        self._n = n
        self._matrix = [set() for _ in range(m)]

    def flip(self) -> List[int]:
        from random import randint
        m, n = self._m, self._n
        row = randint(0, m-1)
        while len(self._matrix[row]) == n:
            row = (row + 1) % m
        
        s = self._matrix[row]
        col = randint(0, n-1)
        while col in s:
            col = (col + 1) % n
        
        s.add(col)
        return [row, col]

    def reset(self) -> None:
        for s in self._matrix:
            s.clear()



# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()