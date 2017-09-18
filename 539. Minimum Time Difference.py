class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def t2m(t):
            return int(t[:2])*60+int(t[3:])
        
        n = len(timePoints)
        st = [False] * (24*60)
        for t in timePoints:
            x=t2m(t)
            if st[x]:
                return 0
            st[x] = True
        
        ret = float('inf')
        zq = []
        for t in range(24*60):
            if st[t]:
                zq.append(t)
                if len(zq)>1:
                    ret = min(ret, zq[-1]-zq[-2])
        ret= min(ret, zq[0] + 24*60-zq[-1])
        return ret
            
        