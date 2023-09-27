class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        dresses = sum(machines)
        n = len(machines)
        if dresses % n != 0:
            return -1
        
        num = dresses // n
        moves = [0] * n
        
        for i in range(n):
            if machines[i] < num:
                moves[i+1] += num - machines[i]
                machines[i+1] -= num - machines[i]
            elif machines[i] > num:
                moves[i] += machines[i] - num
                machines[i+1] += machines[i] - num
        
        return max(moves)
