class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        i = 1
        while i < n and nums[i-1] <= nums[i]:
            i += 1
        
        if i == n:
            return 0
        
        start, end = i-1, i
        minNum, maxNum = nums[i], nums[i-1]
        while i < n:
            minNum = min(minNum, nums[i])
            while start > 0 and minNum < nums[start-1]:
                start -= 1
            
            if nums[i] < maxNum:
                end = i
            else:
                maxNum = nums[i]
            i += 1
        #print(start, end)
        return end-start+1

