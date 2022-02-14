class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses = houses + heaters
        houses.sort()
        heaters = set(heaters)
        n = len(houses)
        left, right = [-1] * n, [-1] * n
        l, r = min(heaters), max(heaters)
        for i in range(n):
            if houses[i] in heaters:
                l = houses[i]
            else:
                left[i] = l
            
            if houses[-i] in heaters:
                r = houses[-i]
            else:
                right[-i] = r
        
        ret = 0
        for i in range(n):
            if houses[i] in heaters:
                continue
            h = houses[i]
            x, y = abs(h - left[i]), abs(h-right[i])
            ret = max(ret, min(x, y))
        return ret
