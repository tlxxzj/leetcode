class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        from collections import defaultdict
        d = defaultdict(int)
        n = len(arr)
        arr.sort()
        ret = 0
        for num in arr:
            if num > 0 and num&1 == 0:
                num2 = num // 2
            else:
                num2 = num * 2
            if d.get(num2, 0) > 0:
                d[num2] -= 1
                ret += 1
            else:
                d[num] += 1
        #print(ret, arr)
        return ret == n//2
        