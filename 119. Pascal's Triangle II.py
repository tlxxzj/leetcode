class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ret = [1]
        for i in xrange(rowIndex):
            st = [1]
            for j in range(i):
                st.append(ret[j]+ret[j+1])
            st.append(1)
            ret = st
        return ret
        