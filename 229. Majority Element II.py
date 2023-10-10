class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        v1, v2 = 0, 0
        num1, num2 = 0, 0
        for num in nums:
            if v1 > 0 and num == num1:
                v1 += 1
            elif v2 > 0 and num == num2:
                v2 += 1
            elif v1 == 0:
                v1 = 1
                num1 = num
            elif v2 == 0:
                v2 = 1
                num2 = num
            else:
                v1 -= 1
                v2 -= 1
        
        res = []
        cnt1, cnt2 = 0, 0
        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
        
        if cnt1 > len(nums)//3:
            res.append(num1)
        if cnt2 > len(nums)//3:
            res.append(num2)
        
        return res
