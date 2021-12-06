class Solution:
    def __init__(self, nums: List[int]):
        self.original_nums = nums[:]
        self.nums = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.original_nums[:]
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        from random import randint
        nums = self.nums
        for i in range(1, len(nums)):
            j = randint(0, i)
            nums[i], nums[j] = nums[j], nums[i]
        return nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()