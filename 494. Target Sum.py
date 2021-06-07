class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        from collections import defaultdict
        sums = defaultdict(int)
        sums[0] = 1
        for num in nums:
            new_sums = defaultdict(int)
            for key, val in sums.items():
                new_sums[key+num] += val
                new_sums[key-num] += val
            sums = new_sums
        return sums[target]