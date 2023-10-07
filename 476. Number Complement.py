class Solution:
    def findComplement(self, num: int) -> int:
        highestBit = 31
        while (1<<highestBit) & num == 0:
            highestBit -= 1
        
        highestBit -= 1
        res = 0
        while highestBit >= 0:
            if (1<<highestBit) & num == 0:
                res |= 1<<highestBit
            highestBit -= 1
        
        return res
