class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = nums[:]
        for i in range(1, n):
            nums[i] *= nums[i-1]
            ret[-i-1] *= ret[-i]
        ret[0] = ret[1]
        for i in range(1, n-1):
            ret[i] = nums[i-1] * ret[i+1]
        ret[-1] = nums[-2]
        return ret