class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        from collections import defaultdict
        def rev(num):
            return int(''.join(reversed(str(num))))
        nums = [num - rev(num) for num in nums]
        count = defaultdict(int)
        ret = 0
        for num in nums:
            ret += count[num]
            count[num] += 1
        return ret % 1000000007
        