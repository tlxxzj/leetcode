class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1, l2 = len(nums1), len(nums2)
        greater = {}
        q = []
        
        for i in range(l2):
            while len(q) > 0 and nums2[i] > nums2[q[-1]]:
                j = q.pop()
                greater[nums2[j]] = nums2[i]
            q.append(i)
        
        ret = []
        for num in nums1:
            ret.append(greater.get(num, -1))
        return ret
        
