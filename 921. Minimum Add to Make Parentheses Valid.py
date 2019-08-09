class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        ret = 0
        cnt = 0
        for c in S:
            if c == '(':
                cnt += 1
            elif cnt > 0:
                cnt -= 1
            else:
                ret += 1
        ret += cnt
        return ret