class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        f = lambda x: x.count(min(x))
        queries = [f(q) for q in queries]
        words = [f(w) for w in words]

        q = [0] * (max(max(words), max(queries)) + 2)
        for w in words:
            q[w] += 1
        
        for i in range(len(q)-2, 0, -1):
            q[i] += q[i+1]
        
        return [q[i+1] for i in queries]