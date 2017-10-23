class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        for i in range(n):
            if nums[i] > 0:
                j = i
                c = 0
                while nums[j] > 0:
                    k = j
                    j = (j + nums[j]) % n
                    nums[k] = 0
                    c += 1
                    if c > 1 and j == i:
                        return True
                    
            elif nums[i] < 0:
                j = i
                c = 0
                while nums[j] < 0:
                    k = j
                    j = (j + nums[j] + n) % n
                    nums[k] = 0
                    c += 1
                    if c > 1 and j == i:
                        return True
                
        return False