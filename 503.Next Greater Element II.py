class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = [-1]*len(nums)
        st = []
        for i in range(len(nums)):
            while len(st)>0 and nums[i] > nums[st[-1]]:
                ret[st.pop()] = nums[i]
            st.append(i)
        for i in range(len(nums)):
            while len(st)>0 and nums[i] > nums[st[-1]]:
                ret[st.pop()] = nums[i]
        return ret
        
        