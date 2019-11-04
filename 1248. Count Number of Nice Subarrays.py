class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ret = 0
        x = 0
        odd = {0:1}
        for num in nums:
            if num % 2 == 1:
                x += 1
            odd[x] = odd.get(x, 0) + 1
        for x in odd:
            y = odd.get(x-k, 0)
            ret += odd[x] * y
        return ret
        