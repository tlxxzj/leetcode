class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        s = 0
        res = -float('inf')
        for i in range(n):
            if i > k-1:
                s -= nums[i-k]
            s += nums[i]
            print(s)
            if i >= k-1:
                res = max(res, s/k)
        return res
