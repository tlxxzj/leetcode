class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}
        for i, num in enumerate(nums):
            if target - num in num_indices:
                return [num_indices[target-num], i]
            num_indices[num] = i
        