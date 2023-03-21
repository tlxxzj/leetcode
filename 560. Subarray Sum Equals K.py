class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sums = {}
        ret = 0
        sum = 0
        for i in range(n):
            sum += nums[i]
            x = sum - k
            if sum == k:
                ret += 1
            ret += sums.get(x, 0)
            sums[sum] = sums.get(sum, 0) + 1
        return ret

    
