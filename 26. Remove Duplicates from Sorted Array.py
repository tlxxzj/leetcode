class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        i = 1
        for j in range(1, n):
            if nums[j] == nums[i-1]:
                continue
            nums[i] = nums[j]
            i += 1
        return i