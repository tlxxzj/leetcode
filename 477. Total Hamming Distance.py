class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        diff = 0
        n = len(nums)
        bit_map = {}
        
        for num in nums:
            while num > 0:
                bit = num & (-num)
                bit_map[bit] = bit_map.get(bit, 0) + 1
                num -= bit
        
        for bit_count in bit_map.values():
            diff += bit_count * (n - bit_count)
        
        return diff