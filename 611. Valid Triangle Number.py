class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # b-a < c < a+b
        
        n = len(nums)
        ret = 0
        nums.sort()
        
        # c > b - a
        def lower(l, r, v):
            x=-1
            while l <= r:
                m = (l+r)/2
                if nums[m]>v:
                    x=m
                    r=m-1
                else:
                    l=m+1
            return x
                    
        # c < a + b
        def upper(l, r, v):
            x=-1
            while l <= r:
                m = (l+r)/2
                if nums[m]<v:
                    x=m
                    l=m+1
                else:
                    r=m-1
            return x
        
        for i in xrange(n):
            for j in xrange(i+1, n):
                lo = lower(j+1, n-1, nums[j]-nums[i])
                up = upper(j+1, n-1, nums[i]+nums[j])
                if lo and up > 0:
                    ret += up-lo+1
        
        return ret
                
        
        
        