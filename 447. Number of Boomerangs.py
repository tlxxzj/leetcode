class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def dis(x, y):
            return (x[0]-y[0])*(x[0]-y[0]) + (x[1]-y[1])*(x[1]-y[1])
        ret = 0
        n = len(points)
        for i in range(n):
            tmp = [-1]
            for j in range(n):
                if i==j:continue
                tmp.append(dis(points[i], points[j]))
            tmp.sort()
            l,r=0,0
            while l < n:
                while r <n and tmp[l]==tmp[r]: r+=1
                m=r-l
                ret += m*(m-1)
                l=r
            
        return ret