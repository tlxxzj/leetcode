class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self._sum = [0] * (n+1)
        self._sum[0] = nums[0]
        for i in range(1, n):
            self._sum[i] = self._sum[i-1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self._sum[right] - self._sum[left-1]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
