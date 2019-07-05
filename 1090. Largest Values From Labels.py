class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        n = len(values)
        vl = []
        for i in range(n):
            vl.append((values[i], labels[i]))
        vl.sort(reverse=True)
        ret = 0
        lb = {}
        for i in range(n):
            if num_wanted <= 0:
                break
            v, l = vl[i][0], vl[i][1]
            lb[l] = lb.get(l, 0) + 1
            if lb[l] <= use_limit:
                num_wanted -= 1
                ret += v
        return ret
        