class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = [nums[0]]

        def lower_bound(l, r, x):
            while l < r:
                m = (l + r) >> 1
                if seq[m] < x:
                    l = m + 1
                else:
                    r = m
            return r
                
        for num in nums:
            i = lower_bound(0, len(seq), num)
            if i == len(seq):
                seq.append(num)
            else:
                seq[i] = min(seq[i], num)

        return len(seq)