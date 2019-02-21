class Solution:
    def repeatedNTimes(self, A: 'List[int]') -> 'int':
        s = set()
        for e in A:
            if e in s:
                return e
            s.add(e)