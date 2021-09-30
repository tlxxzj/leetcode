class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        
        ret = []
        p, size, x = set(), 0, 0
        for c in s:
            size += 1
            if c not in p:
                p.add(c)
                x += count[c]
            x -= 1
            if x == 0:
                ret.append(size)
                p, size, x = set(), 0, 0
        return ret
