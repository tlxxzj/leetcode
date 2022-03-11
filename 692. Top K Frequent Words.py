class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import defaultdict
        from functools import cmp_to_key
        def cmp(a, b):
            if a[1] != b[1]:
                return a[1]-b[1]
            elif a[0] < b[0]:
                return 1
            return -1

        top = defaultdict(int)
        for w in words:
            top[w] += 1
        
        return [w[0] for w in sorted(top.items(), key=cmp_to_key(cmp), reverse=True)[:k]]