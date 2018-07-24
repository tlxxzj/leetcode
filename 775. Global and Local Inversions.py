class Solution:
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        for i, j in enumerate(A):
            if (abs(i - j) > 1):
                return False
        return True
        