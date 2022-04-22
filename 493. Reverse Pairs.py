class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def binarySearch(arr, l, r, x):
            while l < r:
                m = (l + r)// 2
                if arr[m] <= x:
                    l = m + 1
                else:
                    r = m
            return l
        def mergeSort(arr):
            n = len(arr)
            if n <= 1:
                return arr, 0
            m = n // 2
            a, x = mergeSort(arr[:m])
            b, y = mergeSort(arr[m:])
            ret = x + y
            l, r = 0, len(a)
            for num in b:
                l = binarySearch(a,l, r, num * 2)
                ret += len(a) - l
            i, j = 0, 0
            while i < len(a) and j < len(b):
                if a[i] <= b[j]:
                    arr[i+j] = a[i]
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
            return arr, ret
        _, ret = mergeSort(nums)
        return ret

