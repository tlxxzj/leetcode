class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ret = 0
        left, right = 1, -1
        nums_set = set(nums)

        def get_longest_seq(num):
            l, r = num, num
            while l - 1 in nums_set:
                l -= 1
                nums_set.remove(l)
            while r + 1 in nums_set:
                r += 1
                nums_set.remove(r)
            return l, r
        
        for num in nums:
            if left <= num and num <= right:
                continue
            l, r = get_longest_seq(num)
            if r - l + 1 > ret:
                ret = r - l + 1
                left, right = l, r
        
        return ret