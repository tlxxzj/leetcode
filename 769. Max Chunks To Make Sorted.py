class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ret = 0
        n = len(arr)
        i = 0
        while i < n:
            l = arr[i]
            r = arr[i]
            j = i
            while j < n:
                l = min(l, arr[j])
                r = max(r, arr[j])
                if l == i and r == j:
                    j += 1
                    break
                j += 1
            i = j
            ret += 1
        return ret