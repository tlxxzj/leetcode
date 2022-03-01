class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        count = [1] *(n + 1)
        count[-1] = 0

        length = [1] *(n+1)
        length[-1] = 0

        for i in range(n):
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                if length[j] + 1 == length[i]:
                    count[i] += count[j]
                elif length[j] + 1 > length[i]:
                    length[i] = length[j] + 1
                    count[i] = count[j]
        #print(length)
        #print(count)
        max_length = max(length)
        ret = 0
        for i in range(n):
            if length[i] == max_length:
                ret += count[i]
        return ret
