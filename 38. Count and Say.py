class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n<1:
            return ''
        ret = '1'
        for i in range(n-1):
            x = []
            n = len(ret)
            i = 0
            while i < n:
                j = i+1
                while j < n and ret[i] == ret[j]:
                    j += 1
                x.append(str(j-i))
                x.append(ret[i])
                i = j
            ret = ''.join(x)
        return ret
            