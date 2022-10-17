class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        for c in magazine:
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1
        for c in ransomNote:
            if letters.get(c, 0) == 0:
                return False
            else:
                letters[c] -= 1
        return True