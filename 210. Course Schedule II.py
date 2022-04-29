class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        inCount = [0] *  n
        #outCount = [0] * n
        edge = [[] for i in range(n)]
        for a,b in prerequisites:
            inCount[a] += 1
            #outCount[b] += 1
            edge[b].append(a)
        ret = []
        q = []
        for i in range(n):
            if inCount[i] == 0:
                q.append(i)
        
        while len(q) > 0:
            x = q.pop()
            ret.append(x)
            for e in edge[x]:
                inCount[e] -= 1
                if inCount[e] == 0:
                    q.append(e)
        if len(ret) != n:
            ret = []
        return ret
        