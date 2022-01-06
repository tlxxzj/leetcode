class Solution:
    def nextGreaterElement(self, n: int) -> int:
        def next_permutation(arr):
            n = len(arr)
            if n <= 1:
                return False
            i, j = n-2, n-1
            while i >= 0 and arr[i] >= arr[j]:
                i -= 1
                j -= 1
            if i < 0:
                return False
            k = n - 1
            while arr[i] >= arr[k]:
                k -= 1
            arr[i], arr[k] = arr[k], arr[i]
            a, b = j, n-1
            while a < b:
                arr[a], arr[b] = arr[b], arr[a]
                a += 1
                b -= 1
            return True
        digits = list(str(n))
        if next_permutation(digits):
            greater = int(''.join(digits))
            if greater <= (1 << 31)-1:
                return greater
        return -1