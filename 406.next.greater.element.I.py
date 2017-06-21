class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        greater = {}
        for i in nums:
            while len(stack) > 0 and i > stack[-1]:
                greater[stack.pop()] = i
            stack.append(i)
        for i in stack:
            greater[i] = -1
        return [greater[i] for i in findNums]
