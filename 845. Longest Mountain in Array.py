class Solution:
    def longestMountain(self, A: List[int]) -> int:
        ret = 0
        lenA = len(A)
        left = 0
        right = 0
        i = 1
        while i < lenA:
            while i < lenA and A[i] > A[i-1]:
                i += 1
                left += 1
            while i < lenA and A[i] < A[i-1]:
                i += 1
                right += 1
            if left > 0 and right > 0 and left + right + 1 >= 3:
                ret = max(ret, left + right + 1)
            if i < lenA and A[i] == A[i-1]:
                i += 1
            left = right = 0
        
        return ret