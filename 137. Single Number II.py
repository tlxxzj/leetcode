class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        lowbit, highbit = 0, 0
        for num in nums:
            plus = lowbit & num
            lowbit = lowbit ^ num
            highbit = highbit | plus

            reset = lowbit ^ highbit
            lowbit = lowbit & reset
            highbit = highbit & reset

        return lowbit
