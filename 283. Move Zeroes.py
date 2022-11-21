class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, j = 0, 0
        while j < n:
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            j += 1
        while i < n:
            nums[i] = 0
            i += 1
        