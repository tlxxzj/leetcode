class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        def cmp(a, b):
            if a[2] == b[2]:
                return -(a[0] - b[0])
            return a[2] - b[2]
            
        ts = []
        for t in trips:
            ts.append((0, t[0], t[1]))
            ts.append((1, t[0], t[2]))
        ts.sort(cmp=cmp)
        print(ts)
        for t in ts:
            if t[0] == 0:
                capacity -= t[1]
                if capacity < 0:
                    return False
            else:
                capacity += t[1]
        return True
        