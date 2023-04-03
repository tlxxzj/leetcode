class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        count = defaultdict(int)

        nums.sort()
        for num in nums:
            count[num] += 1
        
        ret = 0
        for num in sorted(count.keys()):
            if k == 0 and count[num] > 1:
                ret += 1
            elif k > 0 and num + k in count:
                ret += 1
            elif k < 0 and num - k in count:
                ret += 1

        return ret