class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        one = False
        i = 0
        while i < n:
            if bits[i] == 1:
                one = False
                i += 2
            else:
                one = True
                i += 1
        
        return one
  
