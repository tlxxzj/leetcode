class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        sumNums = sum(nums)
        ret = sum([i * nums[i] for i in range(n)])
        f = ret
        for i in range(0, n-1):
            f = f - sumNums  + n * nums[i]
            ret = max(ret, f)
        return ret