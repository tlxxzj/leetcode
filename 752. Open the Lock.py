class Queue:
    def __init__(self):
        self.a = []
        self.b = []
    
    def append(self, x):
        self.a.append(x)
    
    def pop(self):
        if len(self.b) == 0:
            self.a, self.b = self.b, self.a
            self.b.reverse()
        return self.b.pop()
    
    def __len__(self):
        return len(self.a) + len(self.b)


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        codes = set('0000')
        q = Queue()
        q.append(('0000', 0))
        while len(q) > 0:
            code, step = q.pop()
            if code == target:
                return step
            for i in range(4):
                newcode = [int(num) for num in code]
                newcode[i] = (newcode[i] + 1) % 10
                newcode = ''.join([str(num) for num in newcode])
                if (newcode not in deadends) and (newcode not in codes):
                    codes.add(newcode)
                    q.append((newcode, step + 1))
                newcode = [int(num) for num in code]
                newcode[i] = (newcode[i] - 1) % 10
                newcode = ''.join([str(num) for num in newcode])
                if (newcode not in deadends) and (newcode not in codes):
                    codes.add(newcode)
                    q.append((newcode, step + 1))
        return -1