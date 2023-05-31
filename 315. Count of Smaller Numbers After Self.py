class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        minNum, maxNum = min(nums), max(nums)
        delta = 0
        if minNum <= 0:
            delta = abs(minNum) + 1
        m = maxNum + delta
        n = len(nums)
        for i in range(n):
            nums[i] += delta
        
        c = [0] * (m + 1)
        counts = [0] * n
        for i in range(n-1, -1, -1):
            num = nums[i]
            while num <= m:
                c[num] += 1
                num += -num&num
            
            num = nums[i]-1
            count = 0
            while num > 0:
                count += c[num]
                num -= -num&num
            counts[i] = count
        
        return counts