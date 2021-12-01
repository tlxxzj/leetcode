class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ret = []
        arr = []
        def combination(s, x, y):
            if s == n and y == 0:
                ret.append(arr[:])
            elif s < n and y>0 and 10-x >= y:
                combination(s, x+1, y)
                arr.append(x)
                combination(s+x, x+1, y-1)
                arr.pop()
        combination(0, 1, k)
        return ret