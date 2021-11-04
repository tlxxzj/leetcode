class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ret = 0
        x = 0
        for c in s:
            if c == '(':
                if x > 0:
                    ret += x
                    x = 0
                x -= 1
            else:
                x += 1
        ret += abs(x)
        return ret
            
