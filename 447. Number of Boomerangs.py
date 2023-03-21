class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        d = [{} for i in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                x =  (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
                d[i][x] = d[i].get(x, 0) + 1
                d[j][x] = d[j].get(x, 0) + 1
        
        ret = 0
        for i in range(n):
            for x in d[i].values():
                ret += x * (x - 1)
        return ret
