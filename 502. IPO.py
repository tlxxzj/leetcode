class Solution:
    class Queue:
        def __init__(self):
            from heapq import heappush, heappop
            self.data = []
        
        def push(self, priority, item):
            heappush(self.data, (priority, item))

        def pop(self):
            return heappop(self.data)[1]
        
        def __len__(self):
            return len(self.data)

    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = [(capital[i], profits[i]) for i in range(n)]
        projects.sort(key=lambda x:x[0])

        q = self.Queue()
        i = 0
        while k > 0:
            while i < n and projects[i][0] <= w:
                q.push(-projects[i][1], projects[i][1])
                i += 1
            if len(q) > 0:
                w += q.pop()
                k -= 1
            else:
                break
        return w
            
