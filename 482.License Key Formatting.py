class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace('-', '')
        S = S.upper()
        n = len(S)
        ret = []
        for i in range(n, 0, -K):
            ret.append(S[max(0, i-K):i])
        ret.reverse()
        return '-'.join(ret)