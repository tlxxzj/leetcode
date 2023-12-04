class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        dp = [[0]*(n2+1) for i in range(n1+1)]

        res = 0
        for i in range(n1):
            for j in range(n2):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                res = max(res, dp[i][j])
        
        return res
