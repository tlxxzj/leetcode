class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ret = 0
        rabbits = {}
        for ans in answers:
            if ans == 0:
                ret += 1
            elif ans in rabbits:
                rabbits[ans] = rabbits[ans] - 1
                if rabbits[ans] == 0:
                    del rabbits[ans]
            else:
                rabbits[ans] = ans
                ret += ans+1
        return ret