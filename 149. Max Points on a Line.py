class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        from fractions import Fraction
        inf = float('inf')
        n = len(points)
        if n <= 1:
            return n
        count = [{} for i in range(n)]

        for i in range(n):
            for j in range(i+1, n):
                a = points[i]
                b = points[j]
                if a[1] == b[1]:
                    f = inf
                else:
                    f = Fraction(a[0]-b[0], a[1]-b[1])
                count[i][f] = count[i].get(f, 0) + 1
                count[j][f] = count[j].get(f, 0) + 1
    
        ans = 0
        for i in range(n):
            ans = max(ans, max(count[i].values()) + 1)
        
        return ans
