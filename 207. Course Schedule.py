class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        x = [0] * numCourses
        y = [[] for i in range(numCourses)]
        
        for e in prerequisites:
            a, b = e
            if a == b or a < 0 or a >= numCourses or b < 0 or b >= numCourses:
                return False
            x[a] += 1
            y[b].append(a)
        
        q = []
        for i, k in enumerate(x):
            if k == 0:
                q.append(i)
        
        #print x
        #print y
        cnt = 0
        while len(q) > 0:
            c = q.pop()
            #print c, y[c]
            cnt += 1
            for i in y[c]:
                x[i] -= 1
                if x[i] == 0:
                    q.append(i)
        
        return cnt == numCourses