class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        ret = []
        q = []
        for log in logs:
            id, status, time = log.split(':')
            id = int(id)
            time = int(time)
            if len(q) == 0 or q[-1][0] != id or status == 'start':
                q.append([id, time, 0])
            else:
                t = time - q[-1][1] - q[-1][2] + 1
                if len(q) > 1:
                    q[-2][2] += time - q[-1][1] + 1
                ret.append([id, t])
                q.pop()
        
        d = {}
        for x in ret:
            id, t = x[0], x[1]
            d[id] = d.get(id, 0) + t
        ret = []
        for k in d:
            ret.append([k, d[k]])
        ret.sort()
        return [x[1] for x in ret]
