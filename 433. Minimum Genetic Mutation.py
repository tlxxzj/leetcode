class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        class Queue(object):
            def __init__(self):
                self.f = []
                self.r = []

            def push(self, x):
                self.f.append(x)

            def pop(self):
                if len(self.r) == 0:
                    self.r = self.f
                    self.r.reverse()
                    self.f = []
                return self.r.pop()

            def __len__(self):
                return len(self.f) + len(self.r)
        
        visited = set()
        q = Queue()
        q.push((start, 0))
        visited.add(start)
        while len(q) > 0:
            x, s = q.pop()
            if x == end:
                return s
            s += 1
            for i in range(8):
                for c in "ACGT":
                    x2 = x[0:i] + c + x[i+1:]
                    if (x2 in bank) and (x2 not in visited):
                        visited.add(x2)
                        q.push((x2, s))

        return -1
        