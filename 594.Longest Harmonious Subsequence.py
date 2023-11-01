class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = {}
        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1
        
        ret = 0
        pre = None
        for num in sorted(cnt.keys()):
            if pre != None and pre + 1 == num:
                ret = max(ret, cnt[pre] + cnt[num])
            pre = num
        return ret
