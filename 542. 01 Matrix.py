class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        ret = [[-1 for j in range(n)] for i in range(m)]
        def dis(sx, sy, x, y):
            return abs(sx-x) + abs(sy-y)
        
        self.f, self.r, self.ql = 0, 0, m*n*4
        qlist = range(self.ql)
        def pushq(e):
            qlist[self.r] = e
            self.r = (self.r+1)%self.ql
        
        def popq():
            x=qlist[self.f]
            self.f =(self.f+1)%self.ql
            return x
        
        def qempty():
            return self.f == self.r
        
        def update():
            while not qempty():
                sx, sy, x, y = popq()
                d = abs(sx-x)+abs(sy-y)
                #print self.f, self.r
                if ret[x][y] == -1 or d < ret[x][y]:
                    ret[x][y] = d
                    if x>0:pushq((sx, sy, x-1, y))
                    if x+1<m:pushq((sx, sy, x+1, y))
                    if y>0:pushq((sx, sy, x, y-1))
                    if y+1<n:pushq((sx, sy, x, y+1))

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    #print i, j
                    pushq((i, j, i, j))
        update()
        #print self.f, self.r
        #print qlist[self.f]
        return ret



#S = Solution()
#print S.updateMatrix([[0,0,0],[0,1,0],[0,0,0]])