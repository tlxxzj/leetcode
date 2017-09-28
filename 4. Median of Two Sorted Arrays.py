class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1, l2 = len(nums1), len(nums2)
        n = l1 + l2
        
        def lower_bound(a, l, r, v):
            while l < r:
                m = (l + r) / 2
                if a[m] >= v:
                    r = m
                else:
                    l = m + 1
            return r
        
        def upper_bound(a, l, r, v):
            while l < r:
                m = (l + r) / 2
                if a[m] > v:
                    r = m
                else:
                    l = m + 1
            return r
        
        def get_idx(v):
            i1, r1 = lower_bound(nums1, 0, l1, v), upper_bound(nums1, 0, l1, v)
            i2, r2 = lower_bound(nums2, 0, l2, v), upper_bound(nums2, 0, l2 ,v)
            return [i1 + i2, r1 + r2]
        
        def findkth(a, l, r, k):
            while l < r:
                m = (l + r) / 2
                idx = get_idx(a[m])
                if idx[0] <= k and idx[1] > k:
                    return a[m]
                elif idx[1] <= k:
                    l = m + 1
                else: #idx[0] > k
                    r = m
            return None
        
        def findkth2(k):
            x = findkth(nums1, 0, l1, k)
            if x is None:
                x = findkth(nums2, 0, l2, k)
            return x
        
        if n&1 == 1:
            ret = findkth2(n/2)
        else:
            x = findkth2(n/2 - 1)
            y = findkth2(n/2)
            ret = (x + y) / 2.0
        return ret
            
            
        
        