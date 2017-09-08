class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        
        def lower_bound(st, left, right, v):
            while left < right:
                mid = (left + right)/2
                if st[mid] < v:
                    left = mid + 1
                else:
                    right = mid
            return right
        
        ret = 0
        heaters.sort()
        for h in houses:
            x = lower_bound(heaters, 0, len(heaters)-1, h)
            print x
            a = abs(h-heaters[x])
            if x+1<len(heaters):
                b = abs(h-heaters[x+1])
            else:
                b = a
            if x-1>=0:
                c = abs(h-heaters[x-1])
            else:
                c = a
            ret = max(ret, min([a,b,c]))
        return ret
        