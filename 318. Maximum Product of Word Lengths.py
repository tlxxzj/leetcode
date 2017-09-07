class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words:
            return 0
        n = len(words)
        d = [0] * n
        for i, w in enumerate(words):
            for j, c in enumerate(w):
                d[i] |= 1<<(ord(c)-ord('a'))
        ret = 0
        for i in range(n):
            for j in range(i+1, n):
                if d[i] & d[j] == 0:
                    ret = max(ret, len(words[i])*len(words[j]))
        return ret
        