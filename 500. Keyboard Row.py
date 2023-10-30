class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        def getrow(c):
            if c.lower() in "qwertyuiop":
                return 1
            elif c.lower() in "asdfghjkl":
                return 2
            else:
                return 3
        
        res = []
        for word in words:
            n = len(word)
            r = getrow(word[0])
            i = 1
            while i < n:
                if getrow(word[i]) != r:
                    break
                i += 1
            if i == n:
                res.append(word)
        
        return res
