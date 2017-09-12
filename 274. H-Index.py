class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        citations.sort()
        
        def lower_bound(st, l, r, v):
            x=r
            while l < r:
                m = (l+r)/2
                if st[m]>= v:
                    x= m
                    r = m
                else:
                    l = m + 1
            return x
        
        for h in range(n, 0, -1):
            k = lower_bound(citations, 0, n, h)
            print k
            if n - k >= h:
                return h
        return 0
        
        
        