class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])
        elif n == 2:
            return f"{str(nums[0])}/{str(nums[1])}"
        return f"{str(nums[0])}/({'/'.join(map(str, nums[1:]))})"
        
