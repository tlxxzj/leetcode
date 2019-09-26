class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        cnt = [1] * (n)
        size = [1] * (n)
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if size[j] + 1 > size[i]:
                        size[i] = size[j] + 1
                        cnt[i] = cnt[j]
                    elif size[j] + 1 == size[i]:
                        cnt[i] += cnt[j]
        max_size = max(size)
        ret = 0
        for i in range(n):
            if size[i] == max_size:
                ret += cnt[i]
        return ret
                        