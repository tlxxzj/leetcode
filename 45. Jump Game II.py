class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        step = [-1] * (n)
        step[0] = 0
        
        for i, s in enumerate(nums):
            j = min(i + s, n - 1)
            if step[j] == -1 or step[i] + 1 < step[j]:
                step[j] = step[i] + 1
                for k in range(i+1, j):
                    if step[k] == -1 or step[i] + 1 < step[k]:
                        step[k] = step[i] + 1
        return step[-1]
            
        