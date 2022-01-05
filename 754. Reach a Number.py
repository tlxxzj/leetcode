class Solution:
    def reachNumber(self, target: int) -> int:
        if target < 0:
            target = -target
        ret = 1
        s = 0
        while True:
            s += ret
            if s == target or (s > target and (s-target)%2==0):
                return ret
            ret += 1