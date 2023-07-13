class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for num in nums1:
            d[num] = d.get(num, 0) + 1
        
        res = []
        for num in nums2:
            count = d.get(num, 0)
            if count > 0:
                res.append(num)
                d[num] = count - 1
        
        return res