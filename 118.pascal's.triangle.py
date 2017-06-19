class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <=0: return []
        ret = [[1]]
        for i in range(1, numRows):
            ret.append([1] + [ ret[-1][i] + ret[-1][i+1] for i in range(0, i-1)] + [1])
        return ret