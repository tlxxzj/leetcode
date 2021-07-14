class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ret = []
        for j in range(1, n-1):
            if j > 1 and nums[j] == nums[j-1] and nums[j] == nums[j-2]:
                continue
            i, k = 0, n-1
            if nums[j] == nums[j-1]:
                i = j - 1
            while i < j and k > j:
                x = nums[i] + nums[j] + nums[k]
                if x < 0:
                    i += 1
                elif  x > 0:
                    k -= 1
                else:
                    ret.append([nums[i], nums[j], nums[k]])
                    i += 1
                    k -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
        return ret