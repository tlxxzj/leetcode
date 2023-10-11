class Solution:
    def reverseWords(self, s: str) -> str:
        from functools import reduce
        words = s.split(" ")
        words = map(lambda w: "".join(reversed(w)), words)
        words = reduce(lambda w1, w2: w1 + " " + w2, words)
        return words
