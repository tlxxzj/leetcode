class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        def _generator(chars, n, chars2, i, j):
            if j == combinationLength:
                yield ''.join(chars2)
            elif i < n and combinationLength - j <= n - i:
                chars2[j] = chars[i]
                for s in _generator(chars, n, chars2, i+1, j+1):
                    yield s
                for s in _generator(chars, n, chars2, i+1, j):
                    yield s
        self._generator = _generator(sorted(characters), len(characters), [''] * combinationLength, 0, 0)
        self._next = next(self._generator, None)
        
    def next(self) -> str:
        _next = self._next
        self._next = next(self._generator, None)
        return _next

    def hasNext(self) -> bool:
        return self._next != None


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()