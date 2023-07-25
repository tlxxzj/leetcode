class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        res = 0
        for i in range(0, len(nums), 2):
            res += nums[i+1]
        
        return res