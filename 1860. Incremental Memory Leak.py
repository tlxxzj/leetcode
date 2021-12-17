class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        i = 1
        while i <= memory1 or i <= memory2:
            if memory1 >= i:
                if memory1 >= memory2:
                    memory1 -= i
                else:
                    memory2 -= i
            else:
                memory2 -= i
            #print(i, memory1, memory2)
            i += 1
        return [i, memory1, memory2]