class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minNum = min(nums)
        return sum([num-minNum for num in nums])
        