class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums
        nums.sort()
        ret = [1] * n
        last = [-1] * n
        for i in range(n):
            for j in range(i+1, n):
                if ret[i] < ret[j] or nums[j] % nums[i] != 0:
                    continue
                ret[j] = ret[i] + 1
                last[j] = i
        
        i = ret.index(max(ret))
        r = []
        while i >= 0:
            r.append(nums[i])
            i = last[i]
        #r.sort()
        return r
