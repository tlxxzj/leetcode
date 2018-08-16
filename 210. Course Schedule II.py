class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        n = numCourses
        ret = []
        s_in = [[] for i in range(n)]
        s_out = [0] * n
        for v, u in prerequisites:
            s_in[u].append(v)
            s_out[v] += 1

        q = []
        for i in range(n):
            if s_out[i] == 0:
                q.append(i)

        while len(q) > 0:
            x = q.pop()
            for y in s_in[x]:
                s_out[y] -= 1
                if s_out[y] == 0:
                    q.append(y)

        if len(ret) != n:
            return []
        return ret


