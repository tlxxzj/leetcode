class Solution:
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        sortedA = sorted(A, reverse=True)
        flips = []
        lenA = len(A)
        
        def reverse(arr, l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
            return arr

        for i in range(lenA):
            index = A.index(sortedA[i])
            flips.append(index + 1)
            flips.append(lenA - i)
            reverse(A, 0, index)
            reverse(A, 0, lenA - i - 1)
            
        return flips
        