class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ret = 0
        n = len(nums)

        def upper_bound(l, r, x):
            while l < r:
                m = (l + r) // 2
                if nums[m] <= x:
                    l = m + 1
                else:
                    r = m
            return l
        
        def lower_bound(l, r, x):
            while l < r:
                m = (l + r) // 2
                if nums[m] < x:
                    l = m + 1
                else:
                    r = m
            return l
        
        for i in range(n):
            for j in range(i+1, n):
                ret += lower_bound(j+1, n, nums[i]+nums[j]) - (j+1)

        return ret