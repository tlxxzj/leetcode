class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def reverse(array, a, b):
            while a < b:
                array[a], array[b] = array[b], array[a]
                a += 1
                b -= 1
        
        ret = []
        n = len(arr)
        i = n
        while i > 0:
            j = arr.index(i)
            if j+1 == i:
                i -= 1
                continue
            ret.append(j+1)
            ret.append(i)
            reverse(arr, 0, j)
            reverse(arr, 0, i-1)
        return ret
            