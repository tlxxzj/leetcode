class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ret, cnt = None, 1
        for num in nums:
            if ret == num:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    ret = num
                    cnt = 1
        return ret