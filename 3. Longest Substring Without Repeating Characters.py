class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_len, k = 0, 0
        sub = {}
        for i, c in enumerate(s):
            if c in sub:
                k = max(k, sub[c] + 1)
            sub[c] = i
            sub_len = max(sub_len, i-k+1)
        return sub_len

