class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <=1:
            return
        i = n-1
        while i-1 >= 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()
            return
        j = n-1
        while nums[i-1] >= nums[j]:
            j -= 1
        nums[i-1], nums[j] = nums[j], nums[i-1]
        j = n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        