class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        moves = 0
        A.sort()
        n = len(A)
        for i in range(1, n):
            moves += max(A[i-1]+1-A[i], 0)
            A[i] = max(A[i], A[i-1]+1)
        return moves
