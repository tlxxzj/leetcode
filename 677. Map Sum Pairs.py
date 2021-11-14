class MapSum:
    def __init__(self):
        self._root = [{}, 0]
    def insert(self, key: str, val: int) -> None:
        node = self._root
        for c in key:
            if c not in node[0]:
                node[0][c] = [{}, 0]
            node = node[0][c]
        node[1] = val

    def sum(self, prefix: str) -> int:
        ret = 0
        node = self._root
        for c in prefix:
            if c not in node[0]:
                return 0
            node = node[0][c]
        q = [node]
        while len(q) > 0:
            node = q.pop()
            ret += node[1]
            q += node[0].values()
        return ret
        



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)