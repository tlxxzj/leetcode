class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ret = [0] * n
        funcs = []
        prev_time = -1
        for log in logs:
            id, start, time = log.split(":")
            id, start, time = int(id), start=="start", int(time)
            if start:
                if len(funcs) > 0:
                    ret[funcs[-1]] += time - prev_time
                funcs.append(id)
            else:
                time += 1
                ret[id] += time - prev_time
                funcs.pop()
            prev_time = time
        return ret