class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr, l, r):
            if l >= r:
                return arr[l:r+1]
            m = (l + r) // 2
            a1 = mergeSort(arr, l, m)
            a2 = mergeSort(arr, m+1, r)
            i, j = 0, 0
            l1, l2 = len(a1), len(a2)
            ret = []
            while i < l1 and j < l2:
                if a1[i] <= a2[j]:
                    ret.append(a1[i])
                    i += 1
                else:
                    ret.append(a2[j])
                    j += 1
            if i < l1:
                ret += a1[i:]
            elif j < l2:
                ret += a2[j:]
            return ret
        return mergeSort(nums, 0, len(nums)-1)