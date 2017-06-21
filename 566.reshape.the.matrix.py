class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not nums: return []
        row, col = len(nums), len(nums[0])
        if row * col != r * c:
            return nums
        ret = []
        nums = [j for i in nums for j in i]
        while nums:
            ret.append(nums[:c])
            nums = nums[c:]
        return ret

        
        
        
        