class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [-1] * n
        q = []
        for i in range(0, 2*n):
            i = i % n
            while len(q) > 0 and nums[i] > nums[q[-1]]:
                ret[q.pop()] = nums[i]
            q.append(i)
        return ret
        