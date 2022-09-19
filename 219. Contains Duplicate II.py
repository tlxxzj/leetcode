class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index = {}
        n = len(nums)
        for j in range(n):
            num = nums[j]
            i = index.get(num, -k-1)
            if j - i <= k:
                return True
            index[num] = j
        return False
            