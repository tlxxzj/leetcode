class Solution:

    def __init__(self, nums: List[int]):
        from collections import defaultdict
        self.index = defaultdict(list)
        for i, num in enumerate(nums):
            self.index[num].append(i)


    def pick(self, target: int) -> int:
        from random import choice
        return choice(self.index[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)