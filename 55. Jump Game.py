class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        ans = [False] * n
        ans[0] = True

        m = 0
        for i in range(n):
            if not ans[i]:
                return False
            for j in range(m, min(n, i + nums[i]+1)):
                ans[j] = True
            m = max(m, i + nums[i]+1)
        return ans[-1]
