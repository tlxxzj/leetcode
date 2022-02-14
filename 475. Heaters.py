class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        def binary_search(l, r, val):
            while l <= r:
                m = (l + r) >> 1
                if heaters[m] < val:
                    l = m + 1
                else:
                    r = m - 1
            return l
        
        ret = 0
        for h in houses:
            if  h <= heaters[0]:
                ret = max(ret, heaters[0] - h)
            elif h >= heaters[-1]:
                ret = max(ret, h - heaters[-1])
            else:
                k = binary_search(0, len(heaters)-1, h)
                x = heaters[k] - h
                y = h - heaters[k-1]
                ret = max(ret, min(x, y))
        return ret