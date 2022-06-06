class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m):
            nums1[-i-1] = nums1[m-i-1]
        i, j = 0, 0
        while i < m or j < n:
            if j >= n or (i < m and nums1[i+n] <= nums2[j]):
                nums1[i+j] = nums1[i+n]
                i += 1
            else:
                nums1[i+j] = nums2[j]
                j += 1
        