class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = set()
        n = len(nums)
        def findall(i, l):
            if len(l) >=2:
                    ret.add(tuple(l))
            if i >=n:
                return
            findall(i+1, l)
            if len(l) == 0 or nums[i] >= l[-1]:
                l.append(nums[i])
                findall(i+1, l)
                l.pop()
                
        
        findall(0, [])
        return list(ret)
    
