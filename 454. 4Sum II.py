class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        sum12 = {}
        for i in nums1:
            for j in nums2:
                sum12[i+j] = sum12.get(i+j, 0)+1
        
        for i in nums3:
            for j in nums4:
                k = 0 - i - j
                count += sum12.get(k, 0)
        
        return count