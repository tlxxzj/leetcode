class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        maxDegree = 0
        degree = {}
        left = {}
        right = {}
        index = 0
        for num in nums:
            if num not in left:
                left[num] = index
            right[num] = index
            degree[num] = degree.get(num, 0) + 1
            maxDegree = max(maxDegree, degree[num])
            index += 1
        
        res = len(nums)
        for num, d in degree.items():
            if d == maxDegree:
                res = min(res, right[num]-left[num]+1)
        
        return res
        

        
