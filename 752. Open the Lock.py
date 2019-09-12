class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set([tuple((int(i) for i in d)) for d in deadends])
        if (0,0,0,0) in deadends:
            return -1
        target = tuple((int(i) for i in target))
        wheels = [i for i in range(10)]
        visited = set([(0,0,0,0)])
        import queue
        q = queue.Queue()
        q.put(((0,0,0,0), 0))
        while q.qsize() > 0:
            seq, step = q.get()
            if seq == target:
                return step
            for i in range(4):
                x = wheels[(seq[i]+1)%10]
                seq2 = list(seq)
                seq2[i] = x
                seq2 = tuple(seq2)
                if (seq2 not in visited) and (seq2 not in deadends):
                    visited.add(seq2)
                    q.put((seq2, step+1))
                
                x = wheels[(seq[i]-1)%10]
                seq2 = list(seq)
                seq2[i] = x
                seq2 = tuple(seq2)
                if (seq2 not in visited) and (seq2 not in deadends):
                    visited.add(seq2)
                    q.put((seq2, step+1))
        return -1