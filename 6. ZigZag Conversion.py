class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        ret = [[] for i in range(numRows)]
        n = len(s)
        i = 0
        while i < n:
            for j in range(numRows):
                if i + j < n:
                    ret[j].append(s[i + j])
            i += numRows
            for j in range(numRows-2):
                if i + j < n:
                    ret[numRows -2 -j].append(s[i + j])
            i += numRows - 2
        return ''.join(map(lambda x: ''.join(x), ret))