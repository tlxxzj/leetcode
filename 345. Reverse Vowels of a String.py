class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        n = len(s)
        i, j = 0, n-1
        while i < j:
            while i < j and s[i].lower() not in "aeiou":
                i += 1
            while i < j and s[j].lower() not in "aeiou":
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return "".join(s)