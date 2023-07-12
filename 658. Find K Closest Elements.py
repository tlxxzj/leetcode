class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        n = len(arr)
        l, r = 0, n
        while l < r:
            m = (l + r) // 2
            if x < arr[m]:
                r = m
            else:
                l = m + 1
        
        l = r - 1
        for i in range(k):
            if l < 0 or (r<n and abs(arr[l]-x) > abs(arr[r]-x)):
                res.append(arr[r])
                r+=1
            else:
                res.append(arr[l])
                l -= 1
        res.sort()
        return res
        