class Solution:
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        
        target = abs(target)
        
        sum = 1
        n = 1
        while sum < target:
            n += 1
            sum += n
        
        d = sum - target
        
        if d % 2 == 0:
            return n
        
        while d % 2 != 0:
            n += 1
            sum += n
            d = sum - target
        
        return n