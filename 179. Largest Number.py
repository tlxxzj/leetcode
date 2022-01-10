class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key
        nums = [str(num) for num in nums]
        def cmp(a, b):
            if a == b:
                return 0
            if a + b > b + a:
                return -1
            return 1
        nums.sort(key=cmp_to_key(cmp))
        if nums[0] == '0':
            return '0'
        return ''.join(nums)
            