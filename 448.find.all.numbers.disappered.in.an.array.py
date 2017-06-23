class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        n = len(nums)
        i = 0
        while i < n:
            v = nums[i]
            if nums[v-1] != v:
                nums[v-1], nums[i] = v, nums[v-1]
            else:
                i+=1
        #print nums
        for i in range(n):
            if i+1 != nums[i]:
                ret.append(i+1)            
        return ret