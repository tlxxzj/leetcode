class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        
        return [item[0] for item in sorted(d.items(), key=lambda x: x[1], reverse=True)[:k]]