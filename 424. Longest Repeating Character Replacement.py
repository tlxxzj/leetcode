class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        cnt = [0] * 26
        l, r = 0, 0
        maxc = 0
        while r < n:
            i = ord(s[r])-ord('A')
            cnt[i] += 1
            maxc = max(maxc, cnt[i])
            if r-l+1-maxc > k:
                i = ord(s[l]) - ord('A')
                cnt[i] -= 1
                l += 1
            r += 1
        return r-l
