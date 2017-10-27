class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []
        nums_sorted = sorted(nums)
        bt = [0] * (n + 1)
        ret = []
        
        def get_index(num):
            l, r = 0, n - 1
            while l < r:
                m = (l + r) / 2
                if nums_sorted[m] < num:
                    l = m + 1
                else:
                    r = m
            return l + 1
        
        def add(x):
            while x <= n:
                bt[x] += 1
                x += -x&x
        
        def sumx(x):
            s = 0
            while x > 0:
                s += bt[x]
                x -= -x&x
            return s
                    
        for i in nums[::-1]:
            x = get_index(i)
            print x,
            ret.append(sumx(x - 1))
            add(x)
        
        print bt
        ret.reverse()
        return ret
        
        
            