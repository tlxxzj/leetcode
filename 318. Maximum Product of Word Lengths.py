class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        chars = [0] * n
        orda = ord('a')
        for i in range(n):
            for c in words[i]:
                chars[i]  = chars[i] | (1<<(ord(c) - orda))
        ret = 0
        for i in range(n):
            for j in range(i+1, n):
                if chars[i] & chars[j] > 0:
                    continue
                ret = max(ret, len(words[i]) * len(words[j]))
        return ret