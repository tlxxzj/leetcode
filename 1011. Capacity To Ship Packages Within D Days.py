class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def ship(W, C, D):
            d = 1
            c = 0
            for w in W:
                if w > C or d > D:
                    return False
                elif c + w <= C:
                    c += w
                else:
                    c = w
                    d += 1
            return d <= D
        
        l, r, m = 0, sum(weights), 0
        while l < r:
            m = (l + r) >> 1
            if ship(weights, m, D):
                r = m
            else:
                l = m + 1
        return r
            