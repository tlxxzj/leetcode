class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0, 0]
        d = set()
        for num in nums:
            if num in d:
                res[0] = num
            else:
                d.add(num)
        
        for i in range(1, len(nums)+1):
            if i not in d:
                res[1] = i
                return res