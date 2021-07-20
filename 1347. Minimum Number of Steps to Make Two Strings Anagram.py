class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import defaultdict
        s_chars, t_chars = defaultdict(int), defaultdict(int)
        ret = 0

        for c in s:
            s_chars[c] += 1
        for c in t:
            t_chars[c] += 1
        
        for c, count in t_chars.items():
            ret += max(0, count-s_chars.get(c, 0))
        
        return ret
        