class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ret = []
        for i in range(len(nums)):
            while nums[i] != 0 and i+1 != nums[i]:
                num = nums[i]
                if nums[i] == nums[num-1]:
                    ret.append(num)
                    nums[i] = 0
                    break
                nums[i], nums[num-1] = nums[num-1], nums[i]
        return ret
