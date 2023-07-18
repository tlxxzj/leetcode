class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        res = nums[0] * nums[1] * nums[2]
        for i in range(4):
            product = nums[2-i] * nums[1-i] * nums[0-i]
            res = max(res, product)
        return res