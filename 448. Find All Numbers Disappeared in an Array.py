class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for i in range(n):
            j, k = i, nums[i]-1
            while j+1 != nums[j] and k+1 != nums[k]:
                nums[j], nums[k] = nums[k], nums[j]
                k = nums[j] - 1
        for i in range(n):
            if nums[i] != i+1:
                res.append(i+1)
        return res