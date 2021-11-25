class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        less = 0
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                less += 1
                if (less > 1) or (i-2>=0 and i+1<n and nums[i+1] < nums[i-1] and nums[i] < nums[i-2]):
                    return False
        return True