class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        minNum, maxNum = min(nums), max(nums)
        d = max(1, (maxNum - minNum) // (n - 1))
        buckets = [[-1, -1] for i in range((maxNum-minNum)//d+1)]
        
        for num in nums:
            i = (num - minNum) // d
            if buckets[i][0] == -1:
                buckets[i][0] = num
                buckets[i][1] = num
            else:
                buckets[i][0] = min(buckets[i][0], num)
                buckets[i][1] = max(buckets[i][1], num)
        
        res = 0
        prev = -1
        for i in range(len(buckets)):
            if buckets[i][0] == -1:
                continue
            if prev != -1:
                res = max(res, buckets[i][0] - buckets[prev][1])
            prev = i
        
        return res

        
        
