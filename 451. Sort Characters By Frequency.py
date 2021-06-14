class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import defaultdict
        frequency = defaultdict(int)
        for c in s:
            frequency[c] += 1
        keys = list(frequency.keys())
        keys.sort(key=lambda x: frequency[x], reverse=True)
        keys = [k*frequency[k] for k in keys]
        return ''.join(keys)