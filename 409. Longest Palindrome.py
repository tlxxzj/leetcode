class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        
        odd = 0
        res = 0
        for k, v in count.items():
            if v%2 == 0:
                res += v
            else:
                res += v - 1
                odd += 1
        if odd > 0:
            res += 1
        return res
