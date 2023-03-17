class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        d = [0] * n
        edge = [[] for i in range(n)]
        for a, b in prerequisites:
            d[a] += 1
            edge[b].append(a)
        
        course = 0
        tp = []
        for i in range(n):
            if d[i] == 0:
                tp.append(i)
        
        while len(tp) > 0:
            course += 1
            x = tp.pop()
            for e in edge[x]:
                d[e] -= 1
                if d[e] == 0:
                    tp.append(e)
        
        return course == n
            


        