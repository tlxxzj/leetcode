class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z0, z1, z2 = 0, 0, 0
        for num in nums:
            if num == 0:
                z0 += 1
            elif num == 1:
                z1 += 1
            else:
                z2 += 1
        i = 0
        while z0 > 0:
            nums[i] = 0
            z0 -= 1
            i += 1
        while z1 > 0:
            nums[i] = 1
            z1 -= 1
            i += 1
        while z2 > 0:
            nums[i] = 2
            z2 -= 1
            i += 1
