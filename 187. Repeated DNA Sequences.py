class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        seqs = defaultdict(int)
        res = []
        h = 0
        for i in range(n):
            c = 0
            if s[i] == 'A':
                c = 0
            elif s[i] == 'C':
                c = 1
            elif s[i] == 'G':
                c = 2
            else:
                c = 3
            h = h << 2
            h = h & ((1<<20)-1)
            h = h | c
            if i<9:
                continue
            seqs[h] += 1
            if seqs[h] == 2:
                res.append(s[i-9:i+1])
        return res
