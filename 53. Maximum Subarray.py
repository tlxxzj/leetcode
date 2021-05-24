class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = nums[0]
        for i in nums[1:]:
            currentSum = max(currentSum+i, i)
            maxSum = max(maxSum, currentSum)
        return maxSum