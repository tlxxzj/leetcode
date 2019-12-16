class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        k = len(nums)//3
        return [i for i in d if d[i] > k]