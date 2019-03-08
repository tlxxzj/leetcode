class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ret = []
        lenp = len(pattern)
        for word in words:
            if len(word) == lenp:
                d = {}
                d2 = {}
                for i in range(lenp + 1):
                    if i == lenp:
                        ret.append(word)
                        break
                    if word[i] in d:
                        w = d[word[i]]
                    else:
                        w = d[word[i]] = pattern[i]
                    if pattern[i] in d2:
                        w2 = d2[pattern[i]]
                    else:
                        w2 = d2[pattern[i]] = word[i]
                    if w != pattern[i] or w2 != word[i]:
                        break
        return ret