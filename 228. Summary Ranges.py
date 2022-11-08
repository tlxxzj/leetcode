class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0:
            return []
        ret = []
        start = 0
        for i in range(1, n):
            if nums[i-1] + 1!= nums[i]:
                if nums[start] == nums[i-1]:
                    ret.append(f'{nums[start]}')
                else:
                    ret.append(f'{nums[start]}->{nums[i-1]}')
                start = i
        if nums[start] == nums[-1]:
            ret.append(f'{nums[start]}')
        else:
            ret.append(f'{nums[start]}->{nums[-1]}')
        return ret