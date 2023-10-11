class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        cnt = 0
        for num in nums:
            if num == 1:
                cnt += 1
                res = max(res, cnt)
            else:
                cnt = 0
        return res
