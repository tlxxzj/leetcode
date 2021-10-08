class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = nums[:] + [1]
        r = nums[:] + [1]
        for i in range(n):
            l[i] *= l[i-1]
            j = n - 1 -i
            r[j] *= r[j+1]
        return [l[i-1] * r[i+1] for i in range(n)]