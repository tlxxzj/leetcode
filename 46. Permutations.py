class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        n = len(nums)
        def permutation(start):
            if start == n:
                permutations.append(nums[:])
                return
            for i in range(start, n):
                nums[i], nums[start] = nums[start], nums[i]
                permutation(start+1)
                nums[i], nums[start] = nums[start], nums[i]
        permutation(0)
        return permutations