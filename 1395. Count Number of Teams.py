class Solution:
    def numTeams(self, rating: List[int]) -> int:
        from collections import defaultdict
        n = len(rating)
        greater = defaultdict(int)

        def merge(arr):
            if len(arr) < 2:
                return arr
            m = len(arr) // 2
            a = merge(arr[:m])
            b = merge(arr[m:])
            i, j = 0, 0
            while i < len(a) and j < len(b):
                if a[i] < b[j]:
                    arr[i+j] = a[i]
                    greater[a[i]] += len(b) - j
                    i += 1
                else:
                    arr[i+j] = b[j]
                    j += 1
            while i < len(a):
                arr[i+j] = a[i]
                i += 1
            while j < len(b):
                arr[i+j] = b[j]
                j += 1
            return arr

        merge(rating[:])
        ret = 0
        for i in range(n):
            for j in range(i+1, n):
                if rating[i] < rating[j]:
                    #print(rating[i], rating[j], greater[rating[j]])
                    ret += greater[rating[j]]
                else:
                    ret += n - j - 1 - greater[rating[j]]
        return ret