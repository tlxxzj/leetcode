class Trie:

    def __init__(self):
        self._root = [{}, False]

    def insert(self, word: str) -> None:
        node = self._root
        for c in word:
            if c not in node[0]:
                node[0][c] = [{}, False]
            node = node[0][c]
        node[1] = True

    def search(self, word: str) -> bool:
        node = self._root
        for c in word:
            if c not in node[0]:
                return False
            node = node[0][c]
        return node[1]

    def startsWith(self, prefix: str) -> bool:
        node = self._root
        for c in prefix:
            if c not in node[0]:
                return False
            node = node[0][c]
        q = [node]
        while len(q) > 0:
            node = q.pop()
            if node[1]:
                return True
            q.extend(node[0].values())
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)