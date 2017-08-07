class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        l1, l2 = len(a), len(b)
        if l1 != l2:
            return max(l1, l2)
        if a != b:
            return l1
        return -1
        