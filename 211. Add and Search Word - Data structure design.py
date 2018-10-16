class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node[0] = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def searchWord(node, word, start, end):
            if start == end:
                return 0 in node
            for i in range(start, end):
                c = word[i]
                if c == '.':
                    for k in node:
                        if k != 0 and searchWord(node[k], word, i+1, end):
                            return True
                    return False
                elif c in node:
                    node = node[c]
                else:
                    return False
            return 0 in node
        
        return searchWord(self.root, word, 0, len(word))
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)