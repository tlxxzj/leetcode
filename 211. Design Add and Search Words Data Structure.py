class WordDictionary:

    def __init__(self):
        self.root = [False, {}]

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node[1]:
                node[1][c] = [False, {}]
            node = node[1][c]
        node[0] = True

    def search(self, word: str) -> bool:
        length = len(word)
        q = [[0, self.root]]
        while len(q) > 0:
            i, node = q.pop()
            if i >= length:
                if node[0]:
                    return True
            elif word[i] == '.':
                q += [[i+1, n] for n in node[1].values()]
            elif word[i] in node[1]:
                q.append([i+1, node[1][word[i]]])
        return False



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)