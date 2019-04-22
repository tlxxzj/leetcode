class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def quick_sort(arr, l, r):
            if l >= r: return
            p = arr[l]
            i, j = l, r
            while i < j:
                while i < j and arr[j] >= p:
                    j -= 1
                arr[i] = arr[j]
                while i < j and arr[i] < p:
                    i += 1
                arr[j] = arr[i]
            arr[i] = p
            quick_sort(arr, l, i-1)
            quick_sort(arr, i+1, r)
        
        quick_sort(nums, 0, len(nums)-1)
        return nums
