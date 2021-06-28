class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = [[]]
        for num in nums:
            sets = sets + [s+[num] for s in sets]
        return sets